(define (problem blocky-problem1)
    (:domain blocky-game)
    (:objects
        up right down left
        place11 place21 place31
        place12 place22 place32
        place13 place23 place33
        room1 room2 room3 room4
        entrance11 entrance12
        entrance21 entrance22
        entrance31
        entrance41
        key_black key_yellow key_blue
        black yellow blue
        terminal1
        exit
        person)
    (:init
        (reversed up down)
        (reversed down up)
        (reversed left right)
        (reversed right left)

        (is key_black black)
        (is key_yellow yellow)
        (is key_blue blue)

        (is_key key_black)
        (is_key key_yellow)
        (is_key key_blue)

        (is_exit exit)

        (is_terminal terminal1)
        
        (adjacent place11 place21 right)
        (adjacent place11 place12 down)
        
        (adjacent place21 place31 right)
        (adjacent place21 place22 down)
        (adjacent place21 place11 left)

        (adjacent place31 place32 down)
        (adjacent place31 place21 left)

        (adjacent place12 place22 right)
        (adjacent place12 place13 down)
        (adjacent place12 place11 up)

        (adjacent place22 place32 right)
        (adjacent place22 place23 down)
        (adjacent place22 place21 up)
        (adjacent place22 place12 left)

        (adjacent place32 place33 down)
        (adjacent place32 place31 up)
        (adjacent place32 place22 left)

        (adjacent place13 place23 right)
        (adjacent place13 place12 up)

        (adjacent place23 place33 right)
        (adjacent place23 place22 up)
        (adjacent place23 place13 left)

        (adjacent place33 place32 up)
        (adjacent place33 place23 left)

        (at room1 place12)
        (at room2 place31)
        (at room3 place13)
        (at room4 place33)

        (free place11)
        (free place21)
        
        (free place22)
        (free place32)

        (free place23)

        (passage room1 entrance11 up)
        (passage room1 entrance12 right)

        (passage room2 entrance21 left)
        (passage room2 entrance22 up)

        (passage room3 entrance31 down)

        (passage room4 entrance41 down)

        (has_door entrance11 blue)
        (has_door entrance12 black)

        (has_door entrance21 black)
        (has_door entrance22 yellow)

        (has_door entrance31 blue)
        
        (has_door entrance41 yellow)

        (contains room1 key_black)
        (contains room2 key_yellow)
        (contains room4 key_blue)

        (contains room3 exit)

        (contains room1 terminal1)

        (in person room1))
    (:goal
        (escaped person))
    )