(define (problem problem-experiment_6x6_8_150_7)
    (:domain blocky-game)
        (:objects
            black - colour
            brown - colour
            cyan - colour
            green - colour
            grey - colour
            orange - colour
            turquoise - colour
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
            entrance_35 - entrance
            entrance_36 - entrance
            entrance_37 - entrance
            entrance_38 - entrance
            entrance_39 - entrance
            entrance_4 - entrance
            entrance_40 - entrance
            entrance_41 - entrance
            entrance_42 - entrance
            entrance_43 - entrance
            entrance_44 - entrance
            entrance_45 - entrance
            entrance_46 - entrance
            entrance_47 - entrance
            entrance_5 - entrance
            entrance_6 - entrance
            entrance_7 - entrance
            entrance_8 - entrance
            entrance_9 - entrance
            main_exit - exit
            key_black - key
            key_brown - key
            key_cyan - key
            key_green - key
            key_grey - key
            key_orange - key
            key_turquoise - key
            key_white - key
            player - person
            place11 - place
            place12 - place
            place13 - place
            place14 - place
            place15 - place
            place16 - place
            place21 - place
            place22 - place
            place23 - place
            place24 - place
            place25 - place
            place26 - place
            place31 - place
            place32 - place
            place33 - place
            place34 - place
            place35 - place
            place36 - place
            place41 - place
            place42 - place
            place43 - place
            place44 - place
            place45 - place
            place46 - place
            place51 - place
            place52 - place
            place53 - place
            place54 - place
            place55 - place
            place56 - place
            place61 - place
            place62 - place
            place63 - place
            place64 - place
            place65 - place
            place66 - place
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
            room_24 - room
            room_25 - room
            room_26 - room
            room_27 - room
            room_28 - room
            room_29 - room
            room_3 - room
            room_30 - room
            room_31 - room
            room_32 - room
            room_33 - room
            room_34 - room
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
            
            (adjacent place11 place12 right)
            (adjacent place11 place21 down)
            (adjacent place12 place11 left)
            (adjacent place12 place13 right)
            (adjacent place12 place22 down)
            (adjacent place13 place12 left)
            (adjacent place13 place14 right)
            (adjacent place13 place23 down)
            (adjacent place14 place13 left)
            (adjacent place14 place15 right)
            (adjacent place14 place24 down)
            (adjacent place15 place14 left)
            (adjacent place15 place16 right)
            (adjacent place15 place25 down)
            (adjacent place16 place15 left)
            (adjacent place16 place26 down)
            (adjacent place21 place11 up)
            (adjacent place21 place22 right)
            (adjacent place21 place31 down)
            (adjacent place22 place12 up)
            (adjacent place22 place21 left)
            (adjacent place22 place23 right)
            (adjacent place22 place32 down)
            (adjacent place23 place13 up)
            (adjacent place23 place22 left)
            (adjacent place23 place24 right)
            (adjacent place23 place33 down)
            (adjacent place24 place14 up)
            (adjacent place24 place23 left)
            (adjacent place24 place25 right)
            (adjacent place24 place34 down)
            (adjacent place25 place15 up)
            (adjacent place25 place24 left)
            (adjacent place25 place26 right)
            (adjacent place25 place35 down)
            (adjacent place26 place16 up)
            (adjacent place26 place25 left)
            (adjacent place26 place36 down)
            (adjacent place31 place21 up)
            (adjacent place31 place32 right)
            (adjacent place31 place41 down)
            (adjacent place32 place22 up)
            (adjacent place32 place31 left)
            (adjacent place32 place33 right)
            (adjacent place32 place42 down)
            (adjacent place33 place23 up)
            (adjacent place33 place32 left)
            (adjacent place33 place34 right)
            (adjacent place33 place43 down)
            (adjacent place34 place24 up)
            (adjacent place34 place33 left)
            (adjacent place34 place35 right)
            (adjacent place34 place44 down)
            (adjacent place35 place25 up)
            (adjacent place35 place34 left)
            (adjacent place35 place36 right)
            (adjacent place35 place45 down)
            (adjacent place36 place26 up)
            (adjacent place36 place35 left)
            (adjacent place36 place46 down)
            (adjacent place41 place31 up)
            (adjacent place41 place42 right)
            (adjacent place41 place51 down)
            (adjacent place42 place32 up)
            (adjacent place42 place41 left)
            (adjacent place42 place43 right)
            (adjacent place42 place52 down)
            (adjacent place43 place33 up)
            (adjacent place43 place42 left)
            (adjacent place43 place44 right)
            (adjacent place43 place53 down)
            (adjacent place44 place34 up)
            (adjacent place44 place43 left)
            (adjacent place44 place45 right)
            (adjacent place44 place54 down)
            (adjacent place45 place35 up)
            (adjacent place45 place44 left)
            (adjacent place45 place46 right)
            (adjacent place45 place55 down)
            (adjacent place46 place36 up)
            (adjacent place46 place45 left)
            (adjacent place46 place56 down)
            (adjacent place51 place41 up)
            (adjacent place51 place52 right)
            (adjacent place51 place61 down)
            (adjacent place52 place42 up)
            (adjacent place52 place51 left)
            (adjacent place52 place53 right)
            (adjacent place52 place62 down)
            (adjacent place53 place43 up)
            (adjacent place53 place52 left)
            (adjacent place53 place54 right)
            (adjacent place53 place63 down)
            (adjacent place54 place44 up)
            (adjacent place54 place53 left)
            (adjacent place54 place55 right)
            (adjacent place54 place64 down)
            (adjacent place55 place45 up)
            (adjacent place55 place54 left)
            (adjacent place55 place56 right)
            (adjacent place55 place65 down)
            (adjacent place56 place46 up)
            (adjacent place56 place55 left)
            (adjacent place56 place66 down)
            (adjacent place61 place51 up)
            (adjacent place61 place62 right)
            (adjacent place62 place52 up)
            (adjacent place62 place61 left)
            (adjacent place62 place63 right)
            (adjacent place63 place53 up)
            (adjacent place63 place62 left)
            (adjacent place63 place64 right)
            (adjacent place64 place54 up)
            (adjacent place64 place63 left)
            (adjacent place64 place65 right)
            (adjacent place65 place55 up)
            (adjacent place65 place64 left)
            (adjacent place65 place66 right)
            (adjacent place66 place56 up)
            (adjacent place66 place65 left)
            (at room_0 place11)
            (at room_1 place12)
            (at room_10 place26)
            (at room_11 place31)
            (at room_12 place32)
            (at room_13 place33)
            (at room_14 place34)
            (at room_15 place35)
            (at room_16 place36)
            (at room_17 place41)
            (at room_18 place42)
            (at room_19 place43)
            (at room_2 place13)
            (at room_20 place44)
            (at room_21 place45)
            (at room_22 place46)
            (at room_23 place51)
            (at room_24 place52)
            (at room_25 place53)
            (at room_26 place54)
            (at room_27 place55)
            (at room_28 place56)
            (at room_29 place61)
            (at room_3 place14)
            (at room_30 place62)
            (at room_31 place63)
            (at room_32 place64)
            (at room_33 place65)
            (at room_34 place66)
            (at room_4 place15)
            (at room_5 place16)
            (at room_6 place22)
            (at room_7 place23)
            (at room_8 place24)
            (at room_9 place25)
            (contains room_0 key_grey)
            (contains room_14 key_brown)
            (contains room_19 key_green)
            (contains room_20 key_white)
            (contains room_22 main_exit)
            (contains room_25 key_cyan)
            (contains room_26 key_black)
            (contains room_3 key_turquoise)
            (contains room_34 key_orange)
            (contains room_9 terminal)
            (free place21)
            (has_door entrance_1 grey)
            (has_door entrance_10 grey)
            (has_door entrance_10 turquoise)
            (has_door entrance_10 white)
            (has_door entrance_11 grey)
            (has_door entrance_11 orange)
            (has_door entrance_11 turquoise)
            (has_door entrance_12 grey)
            (has_door entrance_13 grey)
            (has_door entrance_14 grey)
            (has_door entrance_15 grey)
            (has_door entrance_16 grey)
            (has_door entrance_17 grey)
            (has_door entrance_18 grey)
            (has_door entrance_19 grey)
            (has_door entrance_2 grey)
            (has_door entrance_20 orange)
            (has_door entrance_21 white)
            (has_door entrance_22 turquoise)
            (has_door entrance_23 grey)
            (has_door entrance_23 turquoise)
            (has_door entrance_24 grey)
            (has_door entrance_25 white)
            (has_door entrance_26 white)
            (has_door entrance_27 white)
            (has_door entrance_28 turquoise)
            (has_door entrance_28 white)
            (has_door entrance_29 grey)
            (has_door entrance_3 grey)
            (has_door entrance_30 grey)
            (has_door entrance_31 grey)
            (has_door entrance_32 grey)
            (has_door entrance_33 brown)
            (has_door entrance_33 green)
            (has_door entrance_34 brown)
            (has_door entrance_35 turquoise)
            (has_door entrance_36 brown)
            (has_door entrance_37 brown)
            (has_door entrance_38 cyan)
            (has_door entrance_39 cyan)
            (has_door entrance_4 grey)
            (has_door entrance_40 orange)
            (has_door entrance_41 turquoise)
            (has_door entrance_42 white)
            (has_door entrance_43 white)
            (has_door entrance_44 green)
            (has_door entrance_45 turquoise)
            (has_door entrance_46 black)
            (has_door entrance_47 black)
            (has_door entrance_5 grey)
            (has_door entrance_6 grey)
            (has_door entrance_7 grey)
            (has_door entrance_8 grey)
            (has_door entrance_9 grey)
            (in player room_0)
            (is key_black black)
            (is key_brown brown)
            (is key_cyan cyan)
            (is key_green green)
            (is key_grey grey)
            (is key_orange orange)
            (is key_turquoise turquoise)
            (is key_white white)
            (passage room_0 entrance_1 right)
            (passage room_1 entrance_2 left)
            (passage room_1 entrance_3 right)
            (passage room_1 entrance_40 up)
            (passage room_1 entrance_41 down)
            (passage room_10 entrance_12 up)
            (passage room_10 entrance_13 left)
            (passage room_12 entrance_28 up)
            (passage room_12 entrance_29 down)
            (passage room_12 entrance_42 right)
            (passage room_13 entrance_26 up)
            (passage room_13 entrance_27 down)
            (passage room_14 entrance_22 up)
            (passage room_15 entrance_30 up)
            (passage room_15 entrance_31 down)
            (passage room_19 entrance_39 left)
            (passage room_2 entrance_4 left)
            (passage room_2 entrance_5 down)
            (passage room_20 entrance_20 up)
            (passage room_21 entrance_17 up)
            (passage room_21 entrance_18 down)
            (passage room_21 entrance_45 right)
            (passage room_21 entrance_46 left)
            (passage room_22 entrance_47 right)
            (passage room_24 entrance_37 up)
            (passage room_24 entrance_38 right)
            (passage room_25 entrance_34 up)
            (passage room_26 entrance_44 up)
            (passage room_28 entrance_32 up)
            (passage room_28 entrance_33 down)
            (passage room_28 entrance_43 left)
            (passage room_3 entrance_21 right)
            (passage room_30 entrance_35 left)
            (passage room_30 entrance_36 down)
            (passage room_34 entrance_19 up)
            (passage room_34 entrance_24 left)
            (passage room_34 entrance_25 down)
            (passage room_5 entrance_14 right)
            (passage room_5 entrance_15 left)
            (passage room_7 entrance_6 up)
            (passage room_7 entrance_7 right)
            (passage room_8 entrance_16 down)
            (passage room_8 entrance_8 left)
            (passage room_8 entrance_9 right)
            (passage room_9 entrance_10 left)
            (passage room_9 entrance_11 down)
            (passage room_9 entrance_23 right))
        (:goal
            (escaped player))
)
        