(define (problem problem1-serialized)
    (:domain blocky-game)
        (:objects
            blue - colour
            brown - colour
            grey - colour
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
            entrance_2 - entrance
            entrance_3 - entrance
            entrance_4 - entrance
            entrance_5 - entrance
            entrance_6 - entrance
            entrance_7 - entrance
            entrance_8 - entrance
            entrance_9 - entrance
            main_exit - exit
            key_blue - key
            key_brown - key
            key_grey - key
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
            (at room_4 place15)
            (at room_5 place21)
            (at room_6 place22)
            (at room_7 place23)
            (at room_8 place24)
            (at room_9 place25)
            (contains room_14 main_exit)
            (contains room_15 key_blue)
            (contains room_20 key_grey)
            (contains room_5 key_brown)
            (contains room_6 terminal)
            (free place32)
            (has_door entrance_1 brown)
            (has_door entrance_10 brown)
            (has_door entrance_11 brown)
            (has_door entrance_12 brown)
            (has_door entrance_13 blue)
            (has_door entrance_14 blue)
            (has_door entrance_15 brown)
            (has_door entrance_16 brown)
            (has_door entrance_17 brown)
            (has_door entrance_18 grey)
            (has_door entrance_2 brown)
            (has_door entrance_3 brown)
            (has_door entrance_4 brown)
            (has_door entrance_4 grey)
            (has_door entrance_5 brown)
            (has_door entrance_6 brown)
            (has_door entrance_7 brown)
            (has_door entrance_8 brown)
            (has_door entrance_9 brown)
            (in player room_5)
            (is key_blue blue)
            (is key_brown brown)
            (is key_grey grey)
            (passage room_11 entrance_6 up)
            (passage room_11 entrance_7 down)
            (passage room_14 entrance_18 right)
            (passage room_15 entrance_10 right)
            (passage room_16 entrance_8 up)
            (passage room_16 entrance_9 left)
            (passage room_17 entrance_12 up)
            (passage room_17 entrance_13 left)
            (passage room_20 entrance_14 right)
            (passage room_22 entrance_15 up)
            (passage room_22 entrance_16 down)
            (passage room_5 entrance_1 right)
            (passage room_6 entrance_11 down)
            (passage room_6 entrance_2 left)
            (passage room_6 entrance_3 right)
            (passage room_7 entrance_17 up)
            (passage room_7 entrance_4 left)
            (passage room_7 entrance_5 down))
        (:goal
            (escaped(player)))
)
        