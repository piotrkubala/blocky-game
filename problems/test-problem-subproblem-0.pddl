(define (problem test-problem-subproblem-0)
    (:domain blocky-game)
        (:objects
            black - colour
            brown - colour
            gold - colour
            green - colour
            grey - colour
            indigo - colour
            magenta - colour
            navy - colour
            purple - colour
            turquoise - colour
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
            entrance_77 - entrance
            entrance_78 - entrance
            entrance_79 - entrance
            entrance_8 - entrance
            entrance_80 - entrance
            entrance_81 - entrance
            entrance_82 - entrance
            entrance_83 - entrance
            entrance_84 - entrance
            entrance_85 - entrance
            entrance_86 - entrance
            entrance_87 - entrance
            entrance_88 - entrance
            entrance_89 - entrance
            entrance_9 - entrance
            entrance_90 - entrance
            entrance_91 - entrance
            entrance_92 - entrance
            entrance_93 - entrance
            main_exit - exit
            key_black - key
            key_brown - key
            key_gold - key
            key_green - key
            key_grey - key
            key_indigo - key
            key_magenta - key
            key_navy - key
            key_purple - key
            key_turquoise - key
            key_violet - key
            key_yellow - key
            player - person
            place11 - place
            place12 - place
            place13 - place
            place14 - place
            place15 - place
            place16 - place
            place17 - place
            place18 - place
            place21 - place
            place22 - place
            place23 - place
            place24 - place
            place25 - place
            place26 - place
            place27 - place
            place28 - place
            place31 - place
            place32 - place
            place33 - place
            place34 - place
            place35 - place
            place36 - place
            place37 - place
            place38 - place
            place41 - place
            place42 - place
            place43 - place
            place44 - place
            place45 - place
            place46 - place
            place47 - place
            place48 - place
            place51 - place
            place52 - place
            place53 - place
            place54 - place
            place55 - place
            place56 - place
            place57 - place
            place58 - place
            place61 - place
            place62 - place
            place63 - place
            place64 - place
            place65 - place
            place66 - place
            place67 - place
            place68 - place
            place71 - place
            place72 - place
            place73 - place
            place74 - place
            place75 - place
            place76 - place
            place77 - place
            place78 - place
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
            room_48 - room
            room_49 - room
            room_5 - room
            room_50 - room
            room_51 - room
            room_52 - room
            room_53 - room
            room_54 - room
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
            (adjacent place17 place18 right)
            (adjacent place17 place27 down)
            (adjacent place18 place17 left)
            (adjacent place18 place28 down)
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
            (adjacent place27 place28 right)
            (adjacent place27 place37 down)
            (adjacent place28 place18 up)
            (adjacent place28 place27 left)
            (adjacent place28 place38 down)
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
            (adjacent place37 place38 right)
            (adjacent place37 place47 down)
            (adjacent place38 place28 up)
            (adjacent place38 place37 left)
            (adjacent place38 place48 down)
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
            (adjacent place47 place48 right)
            (adjacent place47 place57 down)
            (adjacent place48 place38 up)
            (adjacent place48 place47 left)
            (adjacent place48 place58 down)
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
            (adjacent place57 place58 right)
            (adjacent place57 place67 down)
            (adjacent place58 place48 up)
            (adjacent place58 place57 left)
            (adjacent place58 place68 down)
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
            (adjacent place67 place68 right)
            (adjacent place67 place77 down)
            (adjacent place68 place58 up)
            (adjacent place68 place67 left)
            (adjacent place68 place78 down)
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
            (adjacent place77 place78 right)
            (adjacent place78 place68 up)
            (adjacent place78 place77 left)
            (at room_0 place11)
            (at room_1 place12)
            (at room_10 place23)
            (at room_11 place24)
            (at room_12 place25)
            (at room_13 place26)
            (at room_14 place27)
            (at room_15 place28)
            (at room_16 place31)
            (at room_17 place32)
            (at room_18 place33)
            (at room_19 place34)
            (at room_2 place13)
            (at room_20 place35)
            (at room_21 place36)
            (at room_22 place37)
            (at room_23 place38)
            (at room_24 place41)
            (at room_25 place42)
            (at room_26 place43)
            (at room_27 place44)
            (at room_28 place45)
            (at room_29 place46)
            (at room_3 place14)
            (at room_30 place47)
            (at room_31 place48)
            (at room_32 place51)
            (at room_33 place52)
            (at room_34 place53)
            (at room_35 place54)
            (at room_36 place56)
            (at room_37 place57)
            (at room_38 place58)
            (at room_39 place61)
            (at room_4 place15)
            (at room_40 place62)
            (at room_41 place63)
            (at room_42 place64)
            (at room_43 place65)
            (at room_44 place66)
            (at room_45 place67)
            (at room_46 place68)
            (at room_47 place71)
            (at room_48 place72)
            (at room_49 place73)
            (at room_5 place16)
            (at room_50 place74)
            (at room_51 place75)
            (at room_52 place76)
            (at room_53 place77)
            (at room_54 place78)
            (at room_6 place17)
            (at room_7 place18)
            (at room_8 place21)
            (at room_9 place22)
            (contains room_12 key_magenta)
            (contains room_20 key_purple)
            (contains room_23 key_grey)
            (contains room_24 main_exit)
            (contains room_28 key_navy)
            (contains room_37 terminal)
            (contains room_38 key_black)
            (contains room_39 key_green)
            (contains room_46 key_yellow)
            (contains room_47 key_turquoise)
            (contains room_49 key_gold)
            (contains room_52 key_brown)
            (contains room_54 key_violet)
            (contains room_8 key_indigo)
            (free place55)
            (has_door entrance_1 yellow)
            (has_door entrance_10 yellow)
            (has_door entrance_11 yellow)
            (has_door entrance_12 yellow)
            (has_door entrance_13 yellow)
            (has_door entrance_14 yellow)
            (has_door entrance_15 yellow)
            (has_door entrance_16 navy)
            (has_door entrance_16 yellow)
            (has_door entrance_17 yellow)
            (has_door entrance_18 green)
            (has_door entrance_18 yellow)
            (has_door entrance_19 yellow)
            (has_door entrance_2 black)
            (has_door entrance_2 yellow)
            (has_door entrance_20 yellow)
            (has_door entrance_21 yellow)
            (has_door entrance_22 yellow)
            (has_door entrance_23 yellow)
            (has_door entrance_24 yellow)
            (has_door entrance_25 black)
            (has_door entrance_25 yellow)
            (has_door entrance_26 indigo)
            (has_door entrance_27 indigo)
            (has_door entrance_28 yellow)
            (has_door entrance_29 yellow)
            (has_door entrance_3 yellow)
            (has_door entrance_30 navy)
            (has_door entrance_30 violet)
            (has_door entrance_31 violet)
            (has_door entrance_31 yellow)
            (has_door entrance_32 indigo)
            (has_door entrance_32 magenta)
            (has_door entrance_33 indigo)
            (has_door entrance_33 navy)
            (has_door entrance_34 yellow)
            (has_door entrance_35 yellow)
            (has_door entrance_36 violet)
            (has_door entrance_37 violet)
            (has_door entrance_38 yellow)
            (has_door entrance_39 yellow)
            (has_door entrance_4 green)
            (has_door entrance_4 yellow)
            (has_door entrance_40 indigo)
            (has_door entrance_41 indigo)
            (has_door entrance_42 indigo)
            (has_door entrance_43 indigo)
            (has_door entrance_44 indigo)
            (has_door entrance_45 indigo)
            (has_door entrance_46 violet)
            (has_door entrance_47 violet)
            (has_door entrance_48 black)
            (has_door entrance_49 black)
            (has_door entrance_49 green)
            (has_door entrance_5 brown)
            (has_door entrance_5 purple)
            (has_door entrance_5 turquoise)
            (has_door entrance_5 yellow)
            (has_door entrance_50 yellow)
            (has_door entrance_51 black)
            (has_door entrance_51 magenta)
            (has_door entrance_52 navy)
            (has_door entrance_53 brown)
            (has_door entrance_54 purple)
            (has_door entrance_55 magenta)
            (has_door entrance_55 turquoise)
            (has_door entrance_56 turquoise)
            (has_door entrance_57 brown)
            (has_door entrance_57 navy)
            (has_door entrance_58 navy)
            (has_door entrance_59 turquoise)
            (has_door entrance_6 yellow)
            (has_door entrance_60 purple)
            (has_door entrance_61 purple)
            (has_door entrance_62 black)
            (has_door entrance_63 navy)
            (has_door entrance_64 brown)
            (has_door entrance_65 brown)
            (has_door entrance_66 magenta)
            (has_door entrance_67 black)
            (has_door entrance_67 turquoise)
            (has_door entrance_68 turquoise)
            (has_door entrance_69 green)
            (has_door entrance_7 yellow)
            (has_door entrance_70 green)
            (has_door entrance_71 yellow)
            (has_door entrance_72 gold)
            (has_door entrance_73 gold)
            (has_door entrance_74 brown)
            (has_door entrance_75 magenta)
            (has_door entrance_76 magenta)
            (has_door entrance_77 navy)
            (has_door entrance_78 brown)
            (has_door entrance_79 green)
            (has_door entrance_8 gold)
            (has_door entrance_8 yellow)
            (has_door entrance_80 green)
            (has_door entrance_81 green)
            (has_door entrance_82 magenta)
            (has_door entrance_83 magenta)
            (has_door entrance_84 turquoise)
            (has_door entrance_85 turquoise)
            (has_door entrance_86 black)
            (has_door entrance_87 gold)
            (has_door entrance_88 navy)
            (has_door entrance_89 navy)
            (has_door entrance_9 yellow)
            (has_door entrance_90 turquoise)
            (has_door entrance_91 turquoise)
            (has_door entrance_92 grey)
            (has_door entrance_93 grey)
            (in player room_46)
            (is key_black black)
            (is key_brown brown)
            (is key_gold gold)
            (is key_green green)
            (is key_grey grey)
            (is key_indigo indigo)
            (is key_magenta magenta)
            (is key_navy navy)
            (is key_purple purple)
            (is key_turquoise turquoise)
            (is key_violet violet)
            (is key_yellow yellow)
            (passage room_0 entrance_22 down)
            (passage room_0 entrance_23 left)
            (passage room_1 entrance_74 right)
            (passage room_1 entrance_75 down)
            (passage room_10 entrance_18 down)
            (passage room_10 entrance_19 up)
            (passage room_10 entrance_68 right)
            (passage room_11 entrance_61 up)
            (passage room_11 entrance_62 down)
            (passage room_12 entrance_54 right)
            (passage room_13 entrance_37 down)
            (passage room_13 entrance_38 up)
            (passage room_14 entrance_59 up)
            (passage room_14 entrance_60 down)
            (passage room_16 entrance_20 down)
            (passage room_16 entrance_21 up)
            (passage room_16 entrance_47 right)
            (passage room_16 entrance_48 left)
            (passage room_17 entrance_45 right)
            (passage room_17 entrance_46 left)
            (passage room_20 entrance_53 right)
            (passage room_21 entrance_41 right)
            (passage room_21 entrance_42 left)
            (passage room_23 entrance_73 up)
            (passage room_24 entrance_93 up)
            (passage room_26 entrance_89 up)
            (passage room_26 entrance_90 down)
            (passage room_27 entrance_14 down)
            (passage room_27 entrance_15 left)
            (passage room_28 entrance_49 right)
            (passage room_28 entrance_82 left)
            (passage room_29 entrance_86 right)
            (passage room_29 entrance_87 left)
            (passage room_3 entrance_83 right)
            (passage room_3 entrance_84 down)
            (passage room_30 entrance_8 right)
            (passage room_30 entrance_88 down)
            (passage room_30 entrance_9 left)
            (passage room_31 entrance_50 up)
            (passage room_31 entrance_51 left)
            (passage room_31 entrance_65 right)
            (passage room_32 entrance_66 right)
            (passage room_32 entrance_67 left)
            (passage room_32 entrance_85 up)
            (passage room_33 entrance_16 right)
            (passage room_33 entrance_17 up)
            (passage room_33 entrance_64 left)
            (passage room_35 entrance_25 up)
            (passage room_35 entrance_26 down)
            (passage room_35 entrance_63 left)
            (passage room_36 entrance_43 right)
            (passage room_36 entrance_44 left)
            (passage room_37 entrance_28 right)
            (passage room_37 entrance_32 up)
            (passage room_37 entrance_4 down)
            (passage room_37 entrance_5 left)
            (passage room_38 entrance_31 up)
            (passage room_38 entrance_72 down)
            (passage room_38 entrance_78 right)
            (passage room_38 entrance_79 left)
            (passage room_39 entrance_56 right)
            (passage room_4 entrance_80 right)
            (passage room_4 entrance_81 left)
            (passage room_40 entrance_12 right)
            (passage room_40 entrance_13 up)
            (passage room_40 entrance_71 down)
            (passage room_41 entrance_10 right)
            (passage room_41 entrance_11 left)
            (passage room_43 entrance_6 right)
            (passage room_43 entrance_7 left)
            (passage room_44 entrance_35 right)
            (passage room_44 entrance_36 up)
            (passage room_45 entrance_2 right)
            (passage room_45 entrance_29 left)
            (passage room_45 entrance_3 up)
            (passage room_45 entrance_30 down)
            (passage room_46 entrance_1 left)
            (passage room_47 entrance_55 down)
            (passage room_47 entrance_58 right)
            (passage room_49 entrance_69 up)
            (passage room_5 entrance_33 down)
            (passage room_5 entrance_34 left)
            (passage room_5 entrance_76 up)
            (passage room_50 entrance_91 up)
            (passage room_50 entrance_92 down)
            (passage room_52 entrance_52 up)
            (passage room_54 entrance_27 up)
            (passage room_6 entrance_39 down)
            (passage room_6 entrance_40 left)
            (passage room_6 entrance_70 up)
            (passage room_8 entrance_24 right)
            (passage room_8 entrance_57 left)
            (passage room_8 entrance_77 up))
        (:goal
            (escaped player))
)
        