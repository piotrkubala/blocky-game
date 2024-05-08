(define (domain blocky-game)
    (:requirements :strips)
    (:predicates
        (at ?room ?place)
        (in ?person ?room)
        (contains ?room ?thing)
        (is_key ?thing)
        (is_exit ?thing)
        (adjacent ?place1 ?place2 ?direction)
        (passage ?room ?entrance ?direction)
        (has_door ?entrance ?colour)
        (owned ?thing ?person)
        (is ?key ?colour)
        (reversed ?direction ?reverse_direction)
        (free ?place)
        (escaped ?person))
    (:action go
        :parameters (?person ?room1 ?room2 ?place1 ?place2 ?entrance1 ?entrance2 ?direction ?reverse_direction ?colour ?key)
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
            (is_key ?key)
            (is ?key ?colour))
        :effect (and
            (not (in ?person ?room1))
            (in ?person ?room2)))
    (:action take
        :parameters (?person ?key ?room)
        :precondition (and
            (contains ?room ?key)
            (is_key ?key)
            (in ?person ?room))
        :effect (and
            (not (contains ?room ?key))
            (owned ?key ?person)))
    (:action escape
        :parameters (?person ?exit ?room)
        :precondition (and
            (contains ?room ?exit)
            (is_exit ?exit)
            (in ?person ?room))
        :effect (and
            (escaped ?person)))
    (:action move
        :parameters (?room ?place1 ?place2 ?direction)
        :precondition (and
            (free ?place2)
            (at ?room ?place1)
            (adjacent ?place1 ?place2 ?direction))
        :effect (and
            (free ?place1)
            (not (free ?place2))
            (not (at ?room ?place1))
            (at ?room ?place2)))
)




















