(define (problem problem1-serialized)
    (:domain blocky-game)
        (:objects
            black - colour
            blue - colour
            yellow - colour
            entrance11 - entrance
            entrance12 - entrance
            entrance21 - entrance
            entrance22 - entrance
            entrance31 - entrance
            entrance41 - entrance
            exit - exit
            key_black - key
            key_blue - key
            key_yellow - key
            person - person
            place11 - place
            place12 - place
            place13 - place
            place21 - place
            place22 - place
            place23 - place
            place31 - place
            place32 - place
            place33 - place
            room1 - room
            room2 - room
            room3 - room
            room4 - room
            terminal1 - terminal)
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
            (adjacent place13 place23 down)
            (adjacent place21 place11 up)
            (adjacent place21 place22 right)
            (adjacent place21 place31 down)
            (adjacent place22 place12 up)
            (adjacent place22 place21 left)
            (adjacent place22 place23 right)
            (adjacent place22 place32 down)
            (adjacent place23 place13 up)
            (adjacent place23 place22 left)
            (adjacent place23 place33 down)
            (adjacent place31 place21 up)
            (adjacent place31 place32 right)
            (adjacent place32 place22 up)
            (adjacent place32 place31 left)
            (adjacent place32 place33 right)
            (adjacent place33 place23 up)
            (adjacent place33 place32 left)
            (at room1 place12)
            (at room2 place31)
            (at room3 place13)
            (at room4 place33)
            (contains room1 key_black)
            (contains room1 terminal1)
            (contains room2 key_yellow)
            (contains room3 exit)
            (contains room4 key_blue)
            (free place11)
            (free place21)
            (free place22)
            (free place23)
            (free place32)
            (has_door entrance11 blue)
            (has_door entrance12 black)
            (has_door entrance21 black)
            (has_door entrance22 yellow)
            (has_door entrance31 blue)
            (has_door entrance41 yellow)
            (in person room1)
            (is key_black black)
            (is key_blue blue)
            (is key_yellow yellow)
            (passage room1 entrance11 up)
            (passage room1 entrance12 right)
            (passage room2 entrance21 left)
            (passage room2 entrance22 up)
            (passage room3 entrance31 down)
            (passage room4 entrance41 down))
        (:goal
            (escaped person))
)
        