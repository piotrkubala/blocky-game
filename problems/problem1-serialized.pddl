(define (problem problem1-serialized)
    (:domain blocky-game)
        (:objects
            brown - colour
            cyan - colour
            navy - colour
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
            entrance_21 - entrance
            entrance_3 - entrance
            entrance_4 - entrance
            entrance_5 - entrance
            entrance_6 - entrance
            entrance_7 - entrance
            entrance_8 - entrance
            entrance_9 - entrance
            main_exit - exit
            key_brown - key
            key_cyan - key
            key_navy - key
            key_white - key
            player - person
            place11 - place
            place12 - place
            place13 - place
            place14 - place
            place15 - place
            place21 - place
            place22 - place
            place23 - place
            place24 - place
            place25 - place
            place31 - place
            place32 - place
            place33 - place
            place34 - place
            place35 - place
            place41 - place
            place42 - place
            place43 - place
            place44 - place
            place45 - place
            place51 - place
            place52 - place
            place53 - place
            place54 - place
            place55 - place
            room_0 - room
            room_1 - room
            room_10 - room
            room_11 - room
            room_12 - room
            room_13 - room
            room_14 - room
            room_15 - room
            room_16 - room
            room_17 - room
            room_18 - room
            room_19 - room
            room_2 - room
            room_20 - room
            room_21 - room
            room_22 - room
            room_23 - room
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
            (at room_10 place32)
            (at room_11 place33)
            (at room_12 place34)
            (at room_13 place35)
            (at room_14 place41)
            (at room_15 place42)
            (at room_16 place43)
            (at room_17 place44)
            (at room_18 place45)
            (at room_19 place51)
            (at room_2 place13)
            (at room_20 place52)
            (at room_21 place53)
            (at room_22 place54)
            (at room_23 place55)
            (at room_3 place14)
            (at room_4 place21)
            (at room_5 place22)
            (at room_6 place23)
            (at room_7 place24)
            (at room_8 place25)
            (at room_9 place31)
            (contains room_14 key_navy)
            (contains room_21 key_cyan)
            (contains room_3 key_brown)
            (contains room_4 key_white)
            (contains room_7 terminal)
            (contains room_9 main_exit)
            (free place15)
            (has_door entrance_1 cyan)
            (has_door entrance_10 cyan)
            (has_door entrance_11 cyan)
            (has_door entrance_12 cyan)
            (has_door entrance_13 cyan)
            (has_door entrance_14 cyan)
            (has_door entrance_15 cyan)
            (has_door entrance_16 cyan)
            (has_door entrance_17 cyan)
            (has_door entrance_18 cyan)
            (has_door entrance_19 white)
            (has_door entrance_2 cyan)
            (has_door entrance_20 white)
            (has_door entrance_21 navy)
            (has_door entrance_3 cyan)
            (has_door entrance_4 cyan)
            (has_door entrance_5 cyan)
            (has_door entrance_6 cyan)
            (has_door entrance_7 cyan)
            (has_door entrance_8 cyan)
            (has_door entrance_8 navy)
            (has_door entrance_9 cyan)
            (in player room_21)
            (is key_brown brown)
            (is key_cyan cyan)
            (is key_navy navy)
            (is key_white white)
            (passage room_12 entrance_10 right)
            (passage room_12 entrance_6 down)
            (passage room_12 entrance_7 up)
            (passage room_14 entrance_11 down)
            (passage room_14 entrance_12 left)
            (passage room_16 entrance_2 down)
            (passage room_16 entrance_3 right)
            (passage room_17 entrance_4 left)
            (passage room_17 entrance_5 up)
            (passage room_2 entrance_18 left)
            (passage room_2 entrance_19 right)
            (passage room_21 entrance_1 up)
            (passage room_21 entrance_9 left)
            (passage room_3 entrance_20 left)
            (passage room_4 entrance_13 right)
            (passage room_4 entrance_15 left)
            (passage room_7 entrance_16 left)
            (passage room_7 entrance_17 right)
            (passage room_7 entrance_8 down)
            (passage room_8 entrance_14 right)
            (passage room_9 entrance_21 up))
        (:goal
            (escaped(player)))
)
        