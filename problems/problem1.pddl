(define (problem blocky-problem1)
    (:domain blocky-game)
    (:objects
        up right down left
        place11 place21 place22
        place12 place22 place32
        place13 place23 place33
        room1 room2 room3 room4
        entrance11 entrance12
        entrance21 entrance22
        entrance31
        entrance41
        key_black key_yellow key_blue
        black yellow blue
        exit
        person)
    (:init
        (reversed up down)
        (reversed down up)
        (reversed left right)
        (reversed right left)))