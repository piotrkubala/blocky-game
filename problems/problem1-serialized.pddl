(define (problem problem1-serialized)
    (:domain blocky-game)
        (:objects
            gold - colour
            white - colour
            entrance_1 - entrance
            entrance_10 - entrance
            entrance_11 - entrance
            entrance_12 - entrance
            entrance_13 - entrance
            entrance_14 - entrance
            entrance_15 - entrance
            entrance_16 - entrance
            entrance_17 - entrance
            entrance_18 - entrance
            entrance_19 - entrance
            entrance_2 - entrance
            entrance_20 - entrance
            entrance_3 - entrance
            entrance_4 - entrance
            entrance_5 - entrance
            entrance_6 - entrance
            entrance_7 - entrance
            entrance_8 - entrance
            entrance_9 - entrance
            main_exit - exit
            key_gold - key
            key_white - key
            player - person
            place11 - place
            place12 - place
            place13 - place
            place14 - place
            place21 - place
            place22 - place
            place23 - place
            place24 - place
            place31 - place
            place32 - place
            place33 - place
            place34 - place
            place41 - place
            place42 - place
            place43 - place
            place44 - place
            room_0 - room
            room_1 - room
            room_10 - room
            room_11 - room
            room_12 - room
            room_13 - room
            room_14 - room
            room_2 - room
            room_3 - room
            room_4 - room
            room_5 - room
            room_6 - room
            room_7 - room
            room_8 - room
            room_9 - room
            terminal - terminal)
        (:init
            (reversed right left)
            (reversed up down)
            (reversed down up)
            (reversed left right)
            
            (at room_0 place11)
            (at room_1 place12)
            (at room_10 place34)
            (at room_11 place41)
            (at room_12 place42)
            (at room_13 place43)
            (at room_14 place44)
            (at room_2 place13)
            (at room_3 place14)
            (at room_4 place21)
            (at room_5 place22)
            (at room_6 place23)
            (at room_7 place24)
            (at room_8 place31)
            (at room_9 place32)
            (contains room_1 main_exit)
            (contains room_7 terminal)
            (escaped player)
            (free place33)
            (has_door entrance_1 gold)
            (has_door entrance_10 gold)
            (has_door entrance_11 gold)
            (has_door entrance_12 gold)
            (has_door entrance_13 white)
            (has_door entrance_14 white)
            (has_door entrance_15 gold)
            (has_door entrance_16 gold)
            (has_door entrance_17 gold)
            (has_door entrance_18 gold)
            (has_door entrance_19 white)
            (has_door entrance_2 gold)
            (has_door entrance_20 white)
            (has_door entrance_3 gold)
            (has_door entrance_4 gold)
            (has_door entrance_5 gold)
            (has_door entrance_6 gold)
            (has_door entrance_7 gold)
            (has_door entrance_8 gold)
            (has_door entrance_9 gold)
            (in player room_1)
            (is key_gold gold)
            (is key_white white)
            (owned key_gold player)
            (owned key_white player)
            (passage room_1 entrance_20 right)
            (passage room_10 entrance_2 up)
            (passage room_10 entrance_3 left)
            (passage room_10 entrance_5 right)
            (passage room_11 entrance_12 down)
            (passage room_12 entrance_10 down)
            (passage room_12 entrance_11 up)
            (passage room_12 entrance_15 left)
            (passage room_13 entrance_8 down)
            (passage room_13 entrance_9 up)
            (passage room_14 entrance_6 left)
            (passage room_14 entrance_7 up)
            (passage room_3 entrance_13 right)
            (passage room_5 entrance_18 right)
            (passage room_5 entrance_19 left)
            (passage room_7 entrance_14 left)
            (passage room_7 entrance_4 right)
            (passage room_9 entrance_1 down)
            (passage room_9 entrance_16 right)
            (passage room_9 entrance_17 left))
        (:goal
            (escaped(player)))
)
        