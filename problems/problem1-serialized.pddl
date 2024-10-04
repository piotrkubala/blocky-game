(define (problem problem1-serialized)
    (:domain blocky-game)
        (:objects
            beige - colour
            grey - colour
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
            entrance_22 - entrance
            entrance_23 - entrance
            entrance_24 - entrance
            entrance_25 - entrance
            entrance_3 - entrance
            entrance_4 - entrance
            entrance_5 - entrance
            entrance_6 - entrance
            entrance_7 - entrance
            entrance_8 - entrance
            entrance_9 - entrance
            main_exit - exit
            key_beige - key
            key_grey - key
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
            (at room_10 place31)
            (at room_11 place32)
            (at room_12 place33)
            (at room_13 place34)
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
            (contains room_10 key_white)
            (contains room_18 terminal)
            (contains room_2 key_beige)
            (contains room_23 key_grey)
            (contains room_6 main_exit)
            (free place35)
            (has_door entrance_1 beige)
            (has_door entrance_10 beige)
            (has_door entrance_11 beige)
            (has_door entrance_12 beige)
            (has_door entrance_12 grey)
            (has_door entrance_13 beige)
            (has_door entrance_14 beige)
            (has_door entrance_15 beige)
            (has_door entrance_16 beige)
            (has_door entrance_17 beige)
            (has_door entrance_18 beige)
            (has_door entrance_19 white)
            (has_door entrance_2 beige)
            (has_door entrance_20 white)
            (has_door entrance_21 white)
            (has_door entrance_22 grey)
            (has_door entrance_23 beige)
            (has_door entrance_24 grey)
            (has_door entrance_25 grey)
            (has_door entrance_3 beige)
            (has_door entrance_4 beige)
            (has_door entrance_5 beige)
            (has_door entrance_6 beige)
            (has_door entrance_7 beige)
            (has_door entrance_8 beige)
            (has_door entrance_8 white)
            (has_door entrance_9 beige)
            (in player room_2)
            (is key_beige beige)
            (is key_grey grey)
            (is key_white white)
            (passage room_1 entrance_25 right)
            (passage room_10 entrance_18 right)
            (passage room_12 entrance_21 right)
            (passage room_12 entrance_22 up)
            (passage room_13 entrance_6 left)
            (passage room_13 entrance_7 right)
            (passage room_14 entrance_16 down)
            (passage room_14 entrance_17 left)
            (passage room_15 entrance_14 down)
            (passage room_15 entrance_15 up)
            (passage room_16 entrance_12 down)
            (passage room_16 entrance_13 up)
            (passage room_17 entrance_11 up)
            (passage room_17 entrance_8 left)
            (passage room_17 entrance_9 down)
            (passage room_18 entrance_10 up)
            (passage room_18 entrance_19 right)
            (passage room_2 entrance_1 right)
            (passage room_23 entrance_20 left)
            (passage room_6 entrance_23 down)
            (passage room_6 entrance_24 left)
            (passage room_7 entrance_2 left)
            (passage room_7 entrance_3 down)
            (passage room_8 entrance_4 up)
            (passage room_8 entrance_5 right))
        (:goal
            (escaped(player)))
)
        