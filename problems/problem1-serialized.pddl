(define (problem problem1-serialized)
    (:domain blocky-game)
        (:objects
            main_exit - exit
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
            room_9 - room)
        (:init
            (reversed right left)
            (reversed up down)
            (reversed down up)
            (reversed left right)
            
            (at room_0 place11)
            (at room_1 place12)
            (at room_10 place31)
            (at room_11 place33)
            (at room_12 place34)
            (at room_13 place35)
            (at room_14 place41)
            (at room_15 place42)
            (at room_16 place43)
            (at room_17 place44)
            (at room_18 place45)
            (at room_19 place51)
            (at room_2 place13)
            (at room_20 place52)
            (at room_21 place53)
            (at room_22 place54)
            (at room_23 place55)
            (at room_3 place14)
            (at room_4 place15)
            (at room_5 place21)
            (at room_6 place22)
            (at room_7 place23)
            (at room_8 place24)
            (at room_9 place25)
            (contains room_23 main_exit)
            (free place32)
            (in player room_11))
        (:goal
            (escaped(player)))
)
        