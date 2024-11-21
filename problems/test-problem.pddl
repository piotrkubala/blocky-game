(define (problem test-problem)
    (:domain blocky-game)
        (:objects
            magenta - colour
            turquoise - colour
            violet - colour
            entrance_1 - entrance
            entrance_10 - entrance
            entrance_11 - entrance
            entrance_12 - entrance
            entrance_13 - entrance
            entrance_14 - entrance
            entrance_15 - entrance
            entrance_16 - entrance
            entrance_2 - entrance
            entrance_3 - entrance
            entrance_4 - entrance
            entrance_5 - entrance
            entrance_6 - entrance
            entrance_7 - entrance
            entrance_8 - entrance
            entrance_9 - entrance
            main_exit - exit
            key_magenta - key
            key_turquoise - key
            key_violet - key
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
            room_0 - room
            room_1 - room
            room_10 - room
            room_11 - room
            room_12 - room
            room_13 - room
            room_14 - room
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
            
            (adjacent place11 place12 right)
            (adjacent place11 place21 down)
            (adjacent place12 place11 left)
            (adjacent place12 place13 right)
            (adjacent place12 place22 down)
            (adjacent place13 place12 left)
            (adjacent place13 place14 right)
            (adjacent place13 place23 down)
            (adjacent place14 place13 left)
            (adjacent place14 place24 down)
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
            (adjacent place24 place34 down)
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
            (adjacent place34 place44 down)
            (adjacent place41 place31 up)
            (adjacent place41 place42 right)
            (adjacent place42 place32 up)
            (adjacent place42 place41 left)
            (adjacent place42 place43 right)
            (adjacent place43 place33 up)
            (adjacent place43 place42 left)
            (adjacent place43 place44 right)
            (adjacent place44 place34 up)
            (adjacent place44 place43 left)
            (at room_0 place11)
            (at room_1 place12)
            (at room_10 place34)
            (at room_11 place41)
            (at room_12 place42)
            (at room_13 place43)
            (at room_14 place44)
            (at room_2 place13)
            (at room_3 place14)
            (at room_4 place21)
            (at room_5 place22)
            (at room_6 place23)
            (at room_7 place24)
            (at room_8 place32)
            (at room_9 place33)
            (contains room_0 key_turquoise)
            (contains room_1 key_magenta)
            (contains room_11 key_violet)
            (contains room_12 terminal)
            (contains room_7 main_exit)
            (free place31)
            (has_door entrance_1 magenta)
            (has_door entrance_10 magenta)
            (has_door entrance_11 turquoise)
            (has_door entrance_12 turquoise)
            (has_door entrance_13 turquoise)
            (has_door entrance_14 turquoise)
            (has_door entrance_15 violet)
            (has_door entrance_16 violet)
            (has_door entrance_2 magenta)
            (has_door entrance_3 magenta)
            (has_door entrance_4 magenta)
            (has_door entrance_5 magenta)
            (has_door entrance_6 magenta)
            (has_door entrance_7 magenta)
            (has_door entrance_8 magenta)
            (has_door entrance_9 magenta)
            (in player room_1)
            (is key_magenta magenta)
            (is key_turquoise turquoise)
            (is key_violet violet)
            (passage room_0 entrance_11 up)
            (passage room_0 entrance_9 right)
            (passage room_1 entrance_1 down)
            (passage room_11 entrance_12 down)
            (passage room_12 entrance_10 left)
            (passage room_12 entrance_13 right)
            (passage room_12 entrance_6 up)
            (passage room_2 entrance_7 down)
            (passage room_2 entrance_8 left)
            (passage room_4 entrance_14 left)
            (passage room_4 entrance_15 up)
            (passage room_5 entrance_2 up)
            (passage room_5 entrance_3 down)
            (passage room_7 entrance_16 down)
            (passage room_8 entrance_4 up)
            (passage room_8 entrance_5 down))
        (:goal
            (escaped player))
)
        