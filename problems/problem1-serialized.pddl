(define (problem problem1-serialized)
    (:domain blocky-game)
        (:objects
            cyan - colour
            green - colour
            indigo - colour
            violet - colour
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
            entrance_50 - entrance
            entrance_51 - entrance
            entrance_52 - entrance
            entrance_53 - entrance
            entrance_54 - entrance
            entrance_55 - entrance
            entrance_56 - entrance
            entrance_57 - entrance
            entrance_58 - entrance
            entrance_59 - entrance
            entrance_6 - entrance
            entrance_60 - entrance
            entrance_61 - entrance
            entrance_62 - entrance
            entrance_63 - entrance
            entrance_64 - entrance
            entrance_65 - entrance
            entrance_66 - entrance
            entrance_67 - entrance
            entrance_68 - entrance
            entrance_69 - entrance
            entrance_7 - entrance
            entrance_70 - entrance
            entrance_71 - entrance
            entrance_72 - entrance
            entrance_73 - entrance
            entrance_74 - entrance
            entrance_75 - entrance
            entrance_76 - entrance
            entrance_8 - entrance
            entrance_9 - entrance
            main_exit - exit
            key_cyan - key
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
            place51 - place
            place52 - place
            place53 - place
            place54 - place
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
            (at room_15 place51)
            (at room_16 place52)
            (at room_17 place53)
            (at room_18 place54)
            (at room_2 place13)
            (at room_3 place14)
            (at room_4 place21)
            (at room_5 place22)
            (at room_6 place24)
            (at room_7 place31)
            (at room_8 place32)
            (at room_9 place33)
            (contains room_1 main_exit)
            (contains room_10 terminal)
            (contains room_4 key_cyan)
            (free place23)
            (has_door entrance_18 cyan)
            (has_door entrance_21 cyan)
            (has_door entrance_24 cyan)
            (has_door entrance_34 cyan)
            (has_door entrance_35 cyan)
            (has_door entrance_37 cyan)
            (has_door entrance_38 cyan)
            (has_door entrance_41 cyan)
            (in player room_4)
            (is key_cyan cyan)
            (passage room_0 entrance_1 up)
            (passage room_0 entrance_2 down)
            (passage room_0 entrance_3 left)
            (passage room_0 entrance_4 right)
            (passage room_1 entrance_5 up)
            (passage room_1 entrance_6 down)
            (passage room_1 entrance_7 left)
            (passage room_1 entrance_8 right)
            (passage room_10 entrance_41 up)
            (passage room_10 entrance_42 down)
            (passage room_10 entrance_43 left)
            (passage room_10 entrance_44 right)
            (passage room_11 entrance_45 up)
            (passage room_11 entrance_46 down)
            (passage room_11 entrance_47 left)
            (passage room_11 entrance_48 right)
            (passage room_12 entrance_49 up)
            (passage room_12 entrance_50 down)
            (passage room_12 entrance_51 left)
            (passage room_12 entrance_52 right)
            (passage room_13 entrance_53 up)
            (passage room_13 entrance_54 down)
            (passage room_13 entrance_55 left)
            (passage room_13 entrance_56 right)
            (passage room_14 entrance_57 up)
            (passage room_14 entrance_58 down)
            (passage room_14 entrance_59 left)
            (passage room_14 entrance_60 right)
            (passage room_15 entrance_61 up)
            (passage room_15 entrance_62 down)
            (passage room_15 entrance_63 left)
            (passage room_15 entrance_64 right)
            (passage room_16 entrance_65 up)
            (passage room_16 entrance_66 down)
            (passage room_16 entrance_67 left)
            (passage room_16 entrance_68 right)
            (passage room_17 entrance_69 up)
            (passage room_17 entrance_70 down)
            (passage room_17 entrance_71 left)
            (passage room_17 entrance_72 right)
            (passage room_18 entrance_73 up)
            (passage room_18 entrance_74 down)
            (passage room_18 entrance_75 left)
            (passage room_18 entrance_76 right)
            (passage room_2 entrance_10 down)
            (passage room_2 entrance_11 left)
            (passage room_2 entrance_12 right)
            (passage room_2 entrance_9 up)
            (passage room_3 entrance_13 up)
            (passage room_3 entrance_14 down)
            (passage room_3 entrance_15 left)
            (passage room_3 entrance_16 right)
            (passage room_4 entrance_17 up)
            (passage room_4 entrance_18 down)
            (passage room_4 entrance_19 left)
            (passage room_4 entrance_20 right)
            (passage room_5 entrance_21 up)
            (passage room_5 entrance_22 down)
            (passage room_5 entrance_23 left)
            (passage room_5 entrance_24 right)
            (passage room_6 entrance_25 up)
            (passage room_6 entrance_26 down)
            (passage room_6 entrance_27 left)
            (passage room_6 entrance_28 right)
            (passage room_7 entrance_29 up)
            (passage room_7 entrance_30 down)
            (passage room_7 entrance_31 left)
            (passage room_7 entrance_32 right)
            (passage room_8 entrance_33 up)
            (passage room_8 entrance_34 down)
            (passage room_8 entrance_35 left)
            (passage room_8 entrance_36 right)
            (passage room_9 entrance_37 up)
            (passage room_9 entrance_38 down)
            (passage room_9 entrance_39 left)
            (passage room_9 entrance_40 right))
        (:goal
            (escaped(player)))
)
        