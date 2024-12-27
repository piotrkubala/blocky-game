(define (problem problem-experiment_7x7_6_150_41-subproblem-4)
    (:domain blocky-game)
        (:objects
            grey - colour
            indigo - colour
            magenta - colour
            pink - colour
            white - colour
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
            entrance_48 - entrance
            entrance_49 - entrance
            entrance_5 - entrance
            entrance_6 - entrance
            entrance_7 - entrance
            entrance_8 - entrance
            entrance_9 - entrance
            main_exit - exit
            new_exit - exit
            key_grey - key
            key_indigo - key
            key_magenta - key
            key_pink - key
            key_white - key
            key_yellow - key
            player - person
            place11 - place
            place12 - place
            place13 - place
            place14 - place
            place15 - place
            place16 - place
            place17 - place
            place21 - place
            place22 - place
            place23 - place
            place24 - place
            place25 - place
            place26 - place
            place27 - place
            place31 - place
            place32 - place
            place33 - place
            place34 - place
            place35 - place
            place36 - place
            place37 - place
            place41 - place
            place42 - place
            place43 - place
            place44 - place
            place45 - place
            place46 - place
            place47 - place
            place51 - place
            place52 - place
            place53 - place
            place54 - place
            place55 - place
            place56 - place
            place57 - place
            place61 - place
            place62 - place
            place63 - place
            place64 - place
            place65 - place
            place66 - place
            place67 - place
            place71 - place
            place72 - place
            place73 - place
            place74 - place
            place75 - place
            place76 - place
            place77 - place
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
            room_35 - room
            room_36 - room
            room_37 - room
            room_38 - room
            room_39 - room
            room_4 - room
            room_40 - room
            room_41 - room
            room_42 - room
            room_43 - room
            room_44 - room
            room_45 - room
            room_46 - room
            room_47 - room
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
            (adjacent place16 place17 right)
            (adjacent place16 place26 down)
            (adjacent place17 place16 left)
            (adjacent place17 place27 down)
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
            (adjacent place26 place27 right)
            (adjacent place26 place36 down)
            (adjacent place27 place17 up)
            (adjacent place27 place26 left)
            (adjacent place27 place37 down)
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
            (adjacent place36 place37 right)
            (adjacent place36 place46 down)
            (adjacent place37 place27 up)
            (adjacent place37 place36 left)
            (adjacent place37 place47 down)
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
            (adjacent place46 place47 right)
            (adjacent place46 place56 down)
            (adjacent place47 place37 up)
            (adjacent place47 place46 left)
            (adjacent place47 place57 down)
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
            (adjacent place56 place57 right)
            (adjacent place56 place66 down)
            (adjacent place57 place47 up)
            (adjacent place57 place56 left)
            (adjacent place57 place67 down)
            (adjacent place61 place51 up)
            (adjacent place61 place62 right)
            (adjacent place61 place71 down)
            (adjacent place62 place52 up)
            (adjacent place62 place61 left)
            (adjacent place62 place63 right)
            (adjacent place62 place72 down)
            (adjacent place63 place53 up)
            (adjacent place63 place62 left)
            (adjacent place63 place64 right)
            (adjacent place63 place73 down)
            (adjacent place64 place54 up)
            (adjacent place64 place63 left)
            (adjacent place64 place65 right)
            (adjacent place64 place74 down)
            (adjacent place65 place55 up)
            (adjacent place65 place64 left)
            (adjacent place65 place66 right)
            (adjacent place65 place75 down)
            (adjacent place66 place56 up)
            (adjacent place66 place65 left)
            (adjacent place66 place67 right)
            (adjacent place66 place76 down)
            (adjacent place67 place57 up)
            (adjacent place67 place66 left)
            (adjacent place67 place77 down)
            (adjacent place71 place61 up)
            (adjacent place71 place72 right)
            (adjacent place72 place62 up)
            (adjacent place72 place71 left)
            (adjacent place72 place73 right)
            (adjacent place73 place63 up)
            (adjacent place73 place72 left)
            (adjacent place73 place74 right)
            (adjacent place74 place64 up)
            (adjacent place74 place73 left)
            (adjacent place74 place75 right)
            (adjacent place75 place65 up)
            (adjacent place75 place74 left)
            (adjacent place75 place76 right)
            (adjacent place76 place66 up)
            (adjacent place76 place75 left)
            (adjacent place76 place77 right)
            (adjacent place77 place67 up)
            (adjacent place77 place76 left)
            (at room_0 place23)
            (at room_1 place24)
            (at room_10 place16)
            (at room_11 place62)
            (at room_12 place64)
            (at room_13 place57)
            (at room_14 place47)
            (at room_15 place13)
            (at room_16 place46)
            (at room_17 place76)
            (at room_18 place54)
            (at room_19 place66)
            (at room_2 place26)
            (at room_20 place75)
            (at room_21 place32)
            (at room_22 place15)
            (at room_23 place25)
            (at room_24 place45)
            (at room_25 place34)
            (at room_26 place55)
            (at room_27 place37)
            (at room_28 place51)
            (at room_29 place74)
            (at room_3 place36)
            (at room_30 place73)
            (at room_31 place71)
            (at room_32 place65)
            (at room_33 place63)
            (at room_34 place43)
            (at room_35 place11)
            (at room_36 place21)
            (at room_37 place61)
            (at room_38 place44)
            (at room_39 place67)
            (at room_4 place77)
            (at room_40 place72)
            (at room_41 place53)
            (at room_42 place14)
            (at room_43 place52)
            (at room_44 place22)
            (at room_45 place41)
            (at room_46 place31)
            (at room_47 place33)
            (at room_5 place56)
            (at room_6 place17)
            (at room_7 place12)
            (at room_8 place42)
            (at room_9 place35)
            (contains room_1 main_exit)
            (contains room_35 terminal)
            (contains room_6 new_exit)
            (free place27)
            (has_door entrance_1 indigo)
            (has_door entrance_10 indigo)
            (has_door entrance_11 indigo)
            (has_door entrance_12 indigo)
            (has_door entrance_12 pink)
            (has_door entrance_13 indigo)
            (has_door entrance_13 pink)
            (has_door entrance_14 indigo)
            (has_door entrance_15 indigo)
            (has_door entrance_16 indigo)
            (has_door entrance_17 indigo)
            (has_door entrance_18 indigo)
            (has_door entrance_19 indigo)
            (has_door entrance_2 indigo)
            (has_door entrance_20 indigo)
            (has_door entrance_21 indigo)
            (has_door entrance_22 indigo)
            (has_door entrance_23 indigo)
            (has_door entrance_24 indigo)
            (has_door entrance_25 indigo)
            (has_door entrance_26 pink)
            (has_door entrance_27 pink)
            (has_door entrance_28 pink)
            (has_door entrance_29 pink)
            (has_door entrance_3 indigo)
            (has_door entrance_30 pink)
            (has_door entrance_31 indigo)
            (has_door entrance_32 indigo)
            (has_door entrance_33 indigo)
            (has_door entrance_34 indigo)
            (has_door entrance_35 indigo)
            (has_door entrance_36 indigo)
            (has_door entrance_37 indigo)
            (has_door entrance_38 indigo)
            (has_door entrance_39 indigo)
            (has_door entrance_4 indigo)
            (has_door entrance_40 magenta)
            (has_door entrance_41 magenta)
            (has_door entrance_42 pink)
            (has_door entrance_43 yellow)
            (has_door entrance_44 yellow)
            (has_door entrance_45 indigo)
            (has_door entrance_46 magenta)
            (has_door entrance_47 magenta)
            (has_door entrance_48 white)
            (has_door entrance_49 white)
            (has_door entrance_5 indigo)
            (has_door entrance_6 indigo)
            (has_door entrance_7 indigo)
            (has_door entrance_8 indigo)
            (has_door entrance_9 indigo)
            (in player room_35)
            (is key_grey grey)
            (is key_indigo indigo)
            (is key_magenta magenta)
            (is key_pink pink)
            (is key_white white)
            (is key_yellow yellow)
            (owned key_grey player)
            (owned key_indigo player)
            (owned key_magenta player)
            (owned key_pink player)
            (owned key_white player)
            (owned key_yellow player)
            (passage room_0 entrance_45 left)
            (passage room_0 entrance_46 up)
            (passage room_14 entrance_41 left)
            (passage room_15 entrance_30 down)
            (passage room_15 entrance_31 right)
            (passage room_21 entrance_14 down)
            (passage room_21 entrance_15 up)
            (passage room_22 entrance_42 left)
            (passage room_22 entrance_43 down)
            (passage room_23 entrance_47 down)
            (passage room_23 entrance_48 right)
            (passage room_27 entrance_18 left)
            (passage room_27 entrance_39 down)
            (passage room_27 entrance_40 right)
            (passage room_30 entrance_6 right)
            (passage room_30 entrance_7 down)
            (passage room_31 entrance_4 right)
            (passage room_31 entrance_5 left)
            (passage room_32 entrance_2 right)
            (passage room_32 entrance_3 left)
            (passage room_33 entrance_1 left)
            (passage room_34 entrance_23 left)
            (passage room_34 entrance_24 down)
            (passage room_35 entrance_12 right)
            (passage room_35 entrance_13 up)
            (passage room_35 entrance_19 down)
            (passage room_36 entrance_10 right)
            (passage room_36 entrance_11 left)
            (passage room_36 entrance_22 up)
            (passage room_37 entrance_8 up)
            (passage room_37 entrance_9 left)
            (passage room_41 entrance_20 up)
            (passage room_41 entrance_21 down)
            (passage room_41 entrance_32 left)
            (passage room_42 entrance_35 down)
            (passage room_42 entrance_36 right)
            (passage room_43 entrance_44 up)
            (passage room_44 entrance_33 down)
            (passage room_44 entrance_34 up)
            (passage room_45 entrance_25 up)
            (passage room_45 entrance_26 down)
            (passage room_46 entrance_27 up)
            (passage room_6 entrance_49 left)
            (passage room_7 entrance_28 down)
            (passage room_7 entrance_29 up)
            (passage room_8 entrance_16 down)
            (passage room_8 entrance_17 right)
            (passage room_8 entrance_37 left)
            (passage room_8 entrance_38 up))
        (:goal
            (escaped player))
)
        