(define (problem problem-experiment_5x5_6_150_1-subproblem-4)
    (:domain blocky-game)
        (:objects
            black - colour
            blue - colour
            gold - colour
            navy - colour
            red - colour
            white - colour
            entrance_1 - entrance
            entrance_10 - entrance
            entrance_11 - entrance
            entrance_12 - entrance
            entrance_13 - entrance
            entrance_2 - entrance
            entrance_3 - entrance
            entrance_4 - entrance
            entrance_5 - entrance
            entrance_6 - entrance
            entrance_7 - entrance
            entrance_8 - entrance
            entrance_9 - entrance
            main_exit - exit
            new_exit - exit
            key_black - key
            key_blue - key
            key_gold - key
            key_navy - key
            key_red - key
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
            (adjacent place15 place25 down)
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
            (adjacent place25 place35 down)
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
            (adjacent place35 place45 down)
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
            (adjacent place45 place55 down)
            (adjacent place51 place41 up)
            (adjacent place51 place52 right)
            (adjacent place52 place42 up)
            (adjacent place52 place51 left)
            (adjacent place52 place53 right)
            (adjacent place53 place43 up)
            (adjacent place53 place52 left)
            (adjacent place53 place54 right)
            (adjacent place54 place44 up)
            (adjacent place54 place53 left)
            (adjacent place54 place55 right)
            (adjacent place55 place45 up)
            (adjacent place55 place54 left)
            (at room_0 place33)
            (at room_1 place24)
            (at room_10 place32)
            (at room_11 place43)
            (at room_12 place42)
            (at room_13 place34)
            (at room_14 place14)
            (at room_15 place11)
            (at room_16 place41)
            (at room_17 place45)
            (at room_18 place31)
            (at room_19 place21)
            (at room_2 place44)
            (at room_20 place52)
            (at room_21 place12)
            (at room_22 place55)
            (at room_23 place15)
            (at room_3 place23)
            (at room_4 place54)
            (at room_5 place22)
            (at room_6 place53)
            (at room_7 place25)
            (at room_8 place13)
            (at room_9 place35)
            (contains room_13 terminal)
            (contains room_23 main_exit)
            (contains room_5 new_exit)
            (free place51)
            (has_door entrance_1 black)
            (has_door entrance_10 white)
            (has_door entrance_11 white)
            (has_door entrance_12 gold)
            (has_door entrance_13 gold)
            (has_door entrance_2 black)
            (has_door entrance_2 blue)
            (has_door entrance_3 black)
            (has_door entrance_4 black)
            (has_door entrance_5 navy)
            (has_door entrance_6 navy)
            (has_door entrance_7 blue)
            (has_door entrance_8 blue)
            (has_door entrance_9 blue)
            (in player room_13)
            (is key_black black)
            (is key_blue blue)
            (is key_gold gold)
            (is key_navy navy)
            (is key_red red)
            (is key_white white)
            (owned key_black player)
            (owned key_blue player)
            (owned key_gold player)
            (owned key_navy player)
            (owned key_red player)
            (owned key_white player)
            (passage room_1 entrance_6 left)
            (passage room_13 entrance_12 left)
            (passage room_13 entrance_2 up)
            (passage room_13 entrance_7 down)
            (passage room_15 entrance_4 down)
            (passage room_15 entrance_5 right)
            (passage room_16 entrance_11 right)
            (passage room_19 entrance_3 down)
            (passage room_4 entrance_8 up)
            (passage room_5 entrance_13 right)
            (passage room_6 entrance_10 left)
            (passage room_6 entrance_9 down)
            (passage room_8 entrance_1 down))
        (:goal
            (escaped player))
)
        