(define (problem problem1-serialized)
    (:domain blocky-game)
        (:objects
            green - colour
            violet - colour
            yellow - colour
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
            entrance_22 - entrance
            entrance_23 - entrance
            entrance_24 - entrance
            entrance_25 - entrance
            entrance_26 - entrance
            entrance_27 - entrance
            entrance_28 - entrance
            entrance_29 - entrance
            entrance_3 - entrance
            entrance_30 - entrance
            entrance_31 - entrance
            entrance_32 - entrance
            entrance_33 - entrance
            entrance_34 - entrance
            entrance_4 - entrance
            entrance_5 - entrance
            entrance_6 - entrance
            entrance_7 - entrance
            entrance_8 - entrance
            entrance_9 - entrance
            main_exit - exit
            key_green - key
            key_violet - key
            key_yellow - key
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
            (at room_10 place31)
            (at room_11 place32)
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
            (at room_4 place15)
            (at room_5 place21)
            (at room_6 place22)
            (at room_7 place23)
            (at room_8 place24)
            (at room_9 place25)
            (contains room_12 key_yellow)
            (contains room_19 key_green)
            (contains room_22 main_exit)
            (contains room_4 terminal)
            (contains room_7 key_violet)
            (free place33)
            (has_door entrance_1 violet)
            (has_door entrance_1 yellow)
            (has_door entrance_10 yellow)
            (has_door entrance_11 yellow)
            (has_door entrance_12 yellow)
            (has_door entrance_13 violet)
            (has_door entrance_14 violet)
            (has_door entrance_15 violet)
            (has_door entrance_16 violet)
            (has_door entrance_17 violet)
            (has_door entrance_18 violet)
            (has_door entrance_19 violet)
            (has_door entrance_2 yellow)
            (has_door entrance_20 violet)
            (has_door entrance_21 violet)
            (has_door entrance_22 violet)
            (has_door entrance_23 violet)
            (has_door entrance_24 violet)
            (has_door entrance_25 green)
            (has_door entrance_26 violet)
            (has_door entrance_27 violet)
            (has_door entrance_28 violet)
            (has_door entrance_29 green)
            (has_door entrance_3 yellow)
            (has_door entrance_30 green)
            (has_door entrance_31 yellow)
            (has_door entrance_32 yellow)
            (has_door entrance_33 green)
            (has_door entrance_34 green)
            (has_door entrance_4 yellow)
            (has_door entrance_5 yellow)
            (has_door entrance_6 yellow)
            (has_door entrance_7 yellow)
            (has_door entrance_8 yellow)
            (has_door entrance_9 green)
            (has_door entrance_9 yellow)
            (in player room_12)
            (is key_green green)
            (is key_violet violet)
            (is key_yellow yellow)
            (passage room_0 entrance_18 up)
            (passage room_0 entrance_19 down)
            (passage room_1 entrance_16 right)
            (passage room_1 entrance_17 down)
            (passage room_10 entrance_20 up)
            (passage room_10 entrance_21 down)
            (passage room_12 entrance_1 up)
            (passage room_12 entrance_29 down)
            (passage room_13 entrance_27 up)
            (passage room_13 entrance_28 down)
            (passage room_14 entrance_22 up)
            (passage room_14 entrance_23 down)
            (passage room_17 entrance_32 right)
            (passage room_17 entrance_33 down)
            (passage room_18 entrance_30 up)
            (passage room_18 entrance_31 left)
            (passage room_19 entrance_24 up)
            (passage room_2 entrance_14 right)
            (passage room_2 entrance_15 left)
            (passage room_22 entrance_34 up)
            (passage room_3 entrance_13 left)
            (passage room_3 entrance_4 down)
            (passage room_3 entrance_5 right)
            (passage room_4 entrance_25 right)
            (passage room_4 entrance_6 left)
            (passage room_4 entrance_7 down)
            (passage room_7 entrance_12 right)
            (passage room_8 entrance_10 right)
            (passage room_8 entrance_11 left)
            (passage room_8 entrance_2 down)
            (passage room_8 entrance_3 up)
            (passage room_9 entrance_26 down)
            (passage room_9 entrance_8 up)
            (passage room_9 entrance_9 left))
        (:goal
            (escaped(player)))
)
        