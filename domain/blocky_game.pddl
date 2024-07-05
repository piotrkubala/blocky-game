(define (domain blocky-game)
    (:requirements :strips :typing :derived-predicates)
    (:types
        place - object ; names of places should conform to pattern placeXY, where X and Y have the same number of digits
        room - object
        person - object
        thing - object
        takeable - thing
        key - takeable
        terminal - thing
        exit - thing
        entrance - object
        direction - object
        colour - object)
    (:constants
        up down left right - direction)
    (:predicates
        (at ?room - room
            ?place - place)
        (in ?person - person
            ?room - room)
        (contains ?room - room
            ?thing - thing)
        (adjacent ?place1 - place
            ?place2 - place
            ?direction - direction)
        (passage ?room - room
            ?entrance - entrance
            ?direction - direction)
        (has_door ?entrance - entrance
            ?colour - colour)
        (owned ?thing - takeable
            ?person - person)
        (is ?key - key
            ?colour - colour)
        (reversed ?direction - direction
            ?reverse_direction - direction)
        (free ?place - place)
        (escaped ?person - person))
    ; poor support, should be defined in each problem instance
    ; (:timeless
    ;     (reversed up down)
    ;     (reversed down up)
    ;     (reversed left right)
    ;     (reversed right left))
    (:action go
        :parameters (
            ?person - person
            ?room1 - room
            ?room2 - room
            ?place1 - place
            ?place2 - place
            ?entrance1 - entrance
            ?entrance2 - entrance
            ?direction - direction
            ?reverse_direction - direction
            ?colour - colour
            ?key - key)
        :precondition (and
            (adjacent ?place1 ?place2 ?direction)
            (at ?room1 ?place1)
            (at ?room2 ?place2)
            (passage ?room1 ?entrance1 ?direction)
            (passage ?room2 ?entrance2 ?reverse_direction)
            (has_door ?entrance1 ?colour)
            (has_door ?entrance2 ?colour)
            (in ?person ?room1)
            (owned ?key ?person)
            (is ?key ?colour))
        :effect (and
            (not (in ?person ?room1))
            (in ?person ?room2)))
    (:action take
        :parameters (
            ?person - person
            ?thing - takeable
            ?room - room)
        :precondition (and
            (contains ?room ?thing)
            (in ?person ?room))
        :effect (and
            (not (contains ?room ?thing))
            (owned ?thing ?person)))
    (:action escape
        :parameters (
            ?person - person
            ?exit - exit
            ?room - room)
        :precondition (and
            (contains ?room ?exit)
            (in ?person ?room))
        :effect (and
            (escaped ?person)))
    (:action move
        :parameters (
            ?moved_room - room
            ?place1 - place
            ?place2 - place
            ?direction - direction
            ?person - person
            ?dwelled_room - room
            ?terminal - terminal)
        :precondition (and
            (in ?person ?dwelled_room)
            (contains ?dwelled_room ?terminal)
            (free ?place2)
            (at ?moved_room ?place1)
            (adjacent ?place1 ?place2 ?direction))
        :effect (and
            (free ?place1)
            (not (free ?place2))
            (not (at ?moved_room ?place1))
            (at ?moved_room ?place2)))
)
