(define (problem problem1-serialized)
    (:domain blocky-game)
        (:objects
            black - colour
            green - colour
            magenta - colour
            orange - colour
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
            room_9 - room)
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
            (at room_6 place23)
            (at room_7 place31)
            (at room_8 place32)
            (at room_9 place33)
            (contains room_17 main_exit)
            (free place24)
            (has_door entrance_1 black)
            (has_door entrance_1 green)
            (has_door entrance_1 magenta)
            (has_door entrance_1 orange)
            (has_door entrance_10 black)
            (has_door entrance_10 green)
            (has_door entrance_10 magenta)
            (has_door entrance_10 orange)
            (has_door entrance_11 black)
            (has_door entrance_11 green)
            (has_door entrance_11 magenta)
            (has_door entrance_11 orange)
            (has_door entrance_12 black)
            (has_door entrance_12 green)
            (has_door entrance_12 magenta)
            (has_door entrance_12 orange)
            (has_door entrance_13 black)
            (has_door entrance_13 green)
            (has_door entrance_13 magenta)
            (has_door entrance_13 orange)
            (has_door entrance_14 black)
            (has_door entrance_14 green)
            (has_door entrance_14 magenta)
            (has_door entrance_14 orange)
            (has_door entrance_15 black)
            (has_door entrance_15 green)
            (has_door entrance_15 magenta)
            (has_door entrance_15 orange)
            (has_door entrance_16 black)
            (has_door entrance_16 green)
            (has_door entrance_16 magenta)
            (has_door entrance_16 orange)
            (has_door entrance_17 black)
            (has_door entrance_17 green)
            (has_door entrance_17 magenta)
            (has_door entrance_17 orange)
            (has_door entrance_18 black)
            (has_door entrance_18 green)
            (has_door entrance_18 magenta)
            (has_door entrance_18 orange)
            (has_door entrance_19 black)
            (has_door entrance_19 green)
            (has_door entrance_19 magenta)
            (has_door entrance_19 orange)
            (has_door entrance_2 black)
            (has_door entrance_2 green)
            (has_door entrance_2 magenta)
            (has_door entrance_2 orange)
            (has_door entrance_20 black)
            (has_door entrance_20 green)
            (has_door entrance_20 magenta)
            (has_door entrance_20 orange)
            (has_door entrance_21 black)
            (has_door entrance_21 green)
            (has_door entrance_21 magenta)
            (has_door entrance_21 orange)
            (has_door entrance_22 black)
            (has_door entrance_22 green)
            (has_door entrance_22 magenta)
            (has_door entrance_22 orange)
            (has_door entrance_23 black)
            (has_door entrance_23 green)
            (has_door entrance_23 magenta)
            (has_door entrance_23 orange)
            (has_door entrance_24 black)
            (has_door entrance_24 green)
            (has_door entrance_24 magenta)
            (has_door entrance_24 orange)
            (has_door entrance_25 black)
            (has_door entrance_25 green)
            (has_door entrance_25 magenta)
            (has_door entrance_25 orange)
            (has_door entrance_26 black)
            (has_door entrance_26 green)
            (has_door entrance_26 magenta)
            (has_door entrance_26 orange)
            (has_door entrance_27 black)
            (has_door entrance_27 green)
            (has_door entrance_27 magenta)
            (has_door entrance_27 orange)
            (has_door entrance_28 black)
            (has_door entrance_28 green)
            (has_door entrance_28 magenta)
            (has_door entrance_28 orange)
            (has_door entrance_29 black)
            (has_door entrance_29 green)
            (has_door entrance_29 magenta)
            (has_door entrance_29 orange)
            (has_door entrance_3 black)
            (has_door entrance_3 green)
            (has_door entrance_3 magenta)
            (has_door entrance_3 orange)
            (has_door entrance_30 black)
            (has_door entrance_30 green)
            (has_door entrance_30 magenta)
            (has_door entrance_30 orange)
            (has_door entrance_31 black)
            (has_door entrance_31 green)
            (has_door entrance_31 magenta)
            (has_door entrance_31 orange)
            (has_door entrance_32 black)
            (has_door entrance_32 green)
            (has_door entrance_32 magenta)
            (has_door entrance_32 orange)
            (has_door entrance_33 black)
            (has_door entrance_33 green)
            (has_door entrance_33 magenta)
            (has_door entrance_33 orange)
            (has_door entrance_34 black)
            (has_door entrance_34 green)
            (has_door entrance_34 magenta)
            (has_door entrance_34 orange)
            (has_door entrance_35 black)
            (has_door entrance_35 green)
            (has_door entrance_35 magenta)
            (has_door entrance_35 orange)
            (has_door entrance_36 black)
            (has_door entrance_36 green)
            (has_door entrance_36 magenta)
            (has_door entrance_36 orange)
            (has_door entrance_37 black)
            (has_door entrance_37 green)
            (has_door entrance_37 magenta)
            (has_door entrance_37 orange)
            (has_door entrance_38 black)
            (has_door entrance_38 green)
            (has_door entrance_38 magenta)
            (has_door entrance_38 orange)
            (has_door entrance_39 black)
            (has_door entrance_39 green)
            (has_door entrance_39 magenta)
            (has_door entrance_39 orange)
            (has_door entrance_4 black)
            (has_door entrance_4 green)
            (has_door entrance_4 magenta)
            (has_door entrance_4 orange)
            (has_door entrance_40 black)
            (has_door entrance_40 green)
            (has_door entrance_40 magenta)
            (has_door entrance_40 orange)
            (has_door entrance_41 black)
            (has_door entrance_41 green)
            (has_door entrance_41 magenta)
            (has_door entrance_41 orange)
            (has_door entrance_42 black)
            (has_door entrance_42 green)
            (has_door entrance_42 magenta)
            (has_door entrance_42 orange)
            (has_door entrance_43 black)
            (has_door entrance_43 green)
            (has_door entrance_43 magenta)
            (has_door entrance_43 orange)
            (has_door entrance_44 black)
            (has_door entrance_44 green)
            (has_door entrance_44 magenta)
            (has_door entrance_44 orange)
            (has_door entrance_45 black)
            (has_door entrance_45 green)
            (has_door entrance_45 magenta)
            (has_door entrance_45 orange)
            (has_door entrance_46 black)
            (has_door entrance_46 green)
            (has_door entrance_46 magenta)
            (has_door entrance_46 orange)
            (has_door entrance_47 black)
            (has_door entrance_47 green)
            (has_door entrance_47 magenta)
            (has_door entrance_47 orange)
            (has_door entrance_48 black)
            (has_door entrance_48 green)
            (has_door entrance_48 magenta)
            (has_door entrance_48 orange)
            (has_door entrance_49 black)
            (has_door entrance_49 green)
            (has_door entrance_49 magenta)
            (has_door entrance_49 orange)
            (has_door entrance_5 black)
            (has_door entrance_5 green)
            (has_door entrance_5 magenta)
            (has_door entrance_5 orange)
            (has_door entrance_50 black)
            (has_door entrance_50 green)
            (has_door entrance_50 magenta)
            (has_door entrance_50 orange)
            (has_door entrance_51 black)
            (has_door entrance_51 green)
            (has_door entrance_51 magenta)
            (has_door entrance_51 orange)
            (has_door entrance_52 black)
            (has_door entrance_52 green)
            (has_door entrance_52 magenta)
            (has_door entrance_52 orange)
            (has_door entrance_53 black)
            (has_door entrance_53 green)
            (has_door entrance_53 magenta)
            (has_door entrance_53 orange)
            (has_door entrance_54 black)
            (has_door entrance_54 green)
            (has_door entrance_54 magenta)
            (has_door entrance_54 orange)
            (has_door entrance_55 black)
            (has_door entrance_55 green)
            (has_door entrance_55 magenta)
            (has_door entrance_55 orange)
            (has_door entrance_56 black)
            (has_door entrance_56 green)
            (has_door entrance_56 magenta)
            (has_door entrance_56 orange)
            (has_door entrance_57 black)
            (has_door entrance_57 green)
            (has_door entrance_57 magenta)
            (has_door entrance_57 orange)
            (has_door entrance_58 black)
            (has_door entrance_58 green)
            (has_door entrance_58 magenta)
            (has_door entrance_58 orange)
            (has_door entrance_59 black)
            (has_door entrance_59 green)
            (has_door entrance_59 magenta)
            (has_door entrance_59 orange)
            (has_door entrance_6 black)
            (has_door entrance_6 green)
            (has_door entrance_6 magenta)
            (has_door entrance_6 orange)
            (has_door entrance_60 black)
            (has_door entrance_60 green)
            (has_door entrance_60 magenta)
            (has_door entrance_60 orange)
            (has_door entrance_61 black)
            (has_door entrance_61 green)
            (has_door entrance_61 magenta)
            (has_door entrance_61 orange)
            (has_door entrance_62 black)
            (has_door entrance_62 green)
            (has_door entrance_62 magenta)
            (has_door entrance_62 orange)
            (has_door entrance_63 black)
            (has_door entrance_63 green)
            (has_door entrance_63 magenta)
            (has_door entrance_63 orange)
            (has_door entrance_64 black)
            (has_door entrance_64 green)
            (has_door entrance_64 magenta)
            (has_door entrance_64 orange)
            (has_door entrance_65 black)
            (has_door entrance_65 green)
            (has_door entrance_65 magenta)
            (has_door entrance_65 orange)
            (has_door entrance_66 black)
            (has_door entrance_66 green)
            (has_door entrance_66 magenta)
            (has_door entrance_66 orange)
            (has_door entrance_67 black)
            (has_door entrance_67 green)
            (has_door entrance_67 magenta)
            (has_door entrance_67 orange)
            (has_door entrance_68 black)
            (has_door entrance_68 green)
            (has_door entrance_68 magenta)
            (has_door entrance_68 orange)
            (has_door entrance_69 black)
            (has_door entrance_69 green)
            (has_door entrance_69 magenta)
            (has_door entrance_69 orange)
            (has_door entrance_7 black)
            (has_door entrance_7 green)
            (has_door entrance_7 magenta)
            (has_door entrance_7 orange)
            (has_door entrance_70 black)
            (has_door entrance_70 green)
            (has_door entrance_70 magenta)
            (has_door entrance_70 orange)
            (has_door entrance_71 black)
            (has_door entrance_71 green)
            (has_door entrance_71 magenta)
            (has_door entrance_71 orange)
            (has_door entrance_72 black)
            (has_door entrance_72 green)
            (has_door entrance_72 magenta)
            (has_door entrance_72 orange)
            (has_door entrance_73 black)
            (has_door entrance_73 green)
            (has_door entrance_73 magenta)
            (has_door entrance_73 orange)
            (has_door entrance_74 black)
            (has_door entrance_74 green)
            (has_door entrance_74 magenta)
            (has_door entrance_74 orange)
            (has_door entrance_75 black)
            (has_door entrance_75 green)
            (has_door entrance_75 magenta)
            (has_door entrance_75 orange)
            (has_door entrance_76 black)
            (has_door entrance_76 green)
            (has_door entrance_76 magenta)
            (has_door entrance_76 orange)
            (has_door entrance_8 black)
            (has_door entrance_8 green)
            (has_door entrance_8 magenta)
            (has_door entrance_8 orange)
            (has_door entrance_9 black)
            (has_door entrance_9 green)
            (has_door entrance_9 magenta)
            (has_door entrance_9 orange)
            (in player room_2)
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
        