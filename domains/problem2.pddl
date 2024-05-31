(define (problem blocky-problem2)
    (:domain blocky-game)
    (:objects
        place11 place21 place31 place41 place51 - place
        place12 place22 place32 place42 place52 - place
        place13 place23 place33 place43 place53 - place
        place14 place24 place34 place44 place54 - place
        place15 place25 place35 place45 place55 - place

        room1 room2 room3 room4 room5 - room
        room6 room7 room8 room9 room10 - room

        entrance11 entrance12 entrance13 - entrance
        entrance21 entrance22 entrance23 - entrance
        entrance31 entrance32 - entrance
        entrance41 entrance42 - entrance
        entrance51 - entrance
        entrance61 entrance62 - entrance
        entrance71 entrance72 - entrance
        entrance81 - entrance
        entrance10_1 - entrance

        black yellow blue red green white - colour
        key_black1 key_black2 key_yellow key_blue key_red key_green key_white1 key_white2 - key

        terminal1 terminal2 - terminal
        exit1 exit2 - exit
        person - person)
    (:init
        (reversed right left)
        (reversed up down)
        (reversed down up)
        (reversed left right)

        (is key_black1 black)
        (is key_black2 black)
        (is key_yellow yellow)
        (is key_blue blue)
        (is key_red red)
        (is key_green green)
        (is key_white1 white)
        (is key_white2 white)

        (adjacent place11 place21 right)
        (adjacent place11 place12 down)

        (adjacent place21 place31 right)
        (adjacent place21 place22 down)
        (adjacent place21 place11 left)

        (adjacent place31 place41 right)
        (adjacent place31 place32 down)
        (adjacent place31 place21 left)

        (adjacent place41 place51 right)
        (adjacent place41 place42 down)
        (adjacent place41 place31 left)

        (adjacent place51 place52 down)
        (adjacent place51 place41 left)

        (adjacent place12 place22 right)
        (adjacent place12 place13 down)
        (adjacent place12 place11 up)

        (adjacent place22 place32 right)
        (adjacent place22 place23 down)
        (adjacent place22 place21 up)
        (adjacent place22 place12 left)

        (adjacent place32 place42 right)
        (adjacent place32 place33 down)
        (adjacent place32 place31 up)
        (adjacent place32 place22 left)

        (adjacent place42 place52 right)
        (adjacent place42 place43 down)
        (adjacent place42 place41 up)
        (adjacent place42 place32 left)

        (adjacent place52 place53 down)
        (adjacent place52 place51 up)
        (adjacent place52 place42 left)

        (adjacent place13 place23 right)
        (adjacent place13 place14 down)
        (adjacent place13 place12 up)
        
        (adjacent place23 place33 right)
        (adjacent place23 place24 down)
        (adjacent place23 place22 up)
        (adjacent place23 place13 left)

        (adjacent place33 place43 right)
        (adjacent place33 place34 down)
        (adjacent place33 place32 up)
        (adjacent place33 place23 left)

        (adjacent place43 place53 right)
        (adjacent place43 place44 down)
        (adjacent place43 place42 up)
        (adjacent place43 place33 left)

        (adjacent place53 place54 down)
        (adjacent place53 place52 up)
        (adjacent place53 place43 left)

        (adjacent place14 place24 right)
        (adjacent place14 place15 down)
        (adjacent place14 place13 up)

        (adjacent place24 place34 right)
        (adjacent place24 place25 down)
        (adjacent place24 place23 up)
        (adjacent place24 place14 left)

        (adjacent place34 place44 right)
        (adjacent place34 place35 down)
        (adjacent place34 place33 up)
        (adjacent place34 place24 left)

        (adjacent place44 place54 right)
        (adjacent place44 place45 down)
        (adjacent place44 place43 up)
        (adjacent place44 place34 left)

        (adjacent place54 place55 down)
        (adjacent place54 place53 up)
        (adjacent place54 place44 left)

        (adjacent place15 place25 right)
        (adjacent place15 place14 up)

        (adjacent place25 place35 right)
        (adjacent place25 place24 up)
        (adjacent place25 place15 left)

        (adjacent place35 place45 right)
        (adjacent place35 place34 up)
        (adjacent place35 place25 left)

        (adjacent place45 place55 right)
        (adjacent place45 place44 up)
        (adjacent place45 place35 left)

        (adjacent place55 place54 up)
        (adjacent place55 place45 left)

        (at room1 place15)
        (at room2 place25)
        (at room3 place24)
        (at room4 place23)
        (at room5 place14)
        (at room6 place51)
        (at room7 place34)
        (at room8 place45)
        (at room9 place35)
        (at room10 place41)

        (free place11)
        (free place21)
        (free place31)

        (free place12)
        (free place22)
        (free place32)
        (free place42)
        (free place52)

        (free place13)
        (free place33)
        (free place43)
        (free place53)

        (free place44)
        (free place54)

        (free place55)

        (passage room1 entrance11 up)
        (passage room1 entrance12 right)
        (passage room1 entrance13 down)

        (passage room2 entrance21 right)
        (passage room2 entrance22 down)
        (passage room2 entrance23 left)

        (passage room3 entrance31 up)
        (passage room3 entrance32 down)

        (passage room4 entrance41 up)
        (passage room4 entrance42 right)

        (passage room5 entrance51 left)

        (passage room6 entrance61 right)
        (passage room6 entrance62 left)

        (passage room7 entrance71 up)
        (passage room7 entrance72 left)

        (passage room8 entrance81 down)

        (passage room10 entrance10_1 right)

        (has_door entrance11 yellow)
        (has_door entrance11 green)

        (has_door entrance12 green)

        (has_door entrance13 white)

        (has_door entrance22 green)
        (has_door entrance23 green)

        (has_door entrance31 green)
        (has_door entrance32 black)

        (has_door entrance41 white)
        (has_door entrance42 blue)

        (has_door entrance51 white)

        (has_door entrance61 white)
        (has_door entrance62 blue)

        (has_door entrance71 black)
        (has_door entrance72 red)

        (has_door entrance81 yellow)

        (has_door entrance10_1 red)

        (contains room1 key_green)
        
        (contains room3 key_yellow)

        (contains room4 key_black2)
        (contains room4 key_white1)

        (contains room7 key_blue)

        (contains room8 key_black1)
        (contains room8 key_red)

        (contains room10 key_white2)

        (contains room5 exit1)
        (contains room9 exit2)

        (contains room2 terminal1)
        (contains room10 terminal2)

        (in person room1))
    (:goal
        (escaped person))
)