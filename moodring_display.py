from sense_hat import SenseHat

sense = SenseHat()

def mood_clear():
    sense.clear()

def mood_ring(mood):
    mood_color = int(abs(mood) * 255)

    X = (0, 0, 0)
    if mood < 0:
        O = (255, 0, 0)
    else:
        O = (0, 255, 0)


    ring0 = [
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, O, O, X, X, X,
        X, X, X, O, O, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X
        ]

    ring1 = [
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, O, O, O, O, X, X,
        X, X, O, O, O, O, X, X,
        X, X, O, O, O, O, X, X,
        X, X, O, O, O, O, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X
        ]

    ring2 = [
        X, X, X, X, X, X, X, X,
        X, O, O, O, O, O, O, X,
        X, O, O, O, O, O, O, X,
        X, O, O, O, O, O, O, X,
        X, O, O, O, O, O, O, X,
        X, O, O, O, O, O, O, X,
        X, O, O, O, O, O, O, X,
        X, X, X, X, X, X, X, X
        ]

    ring3 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ]

    if mood_color < 60:
        sense.set_pixels(ring0)

    elif mood_color < 120:
        sense.set_pixels(ring1)

    elif mood_color < 180:
        sense.set_pixels(ring2)

    else:
        sense.set_pixels(ring3)

mood_ring(0.1)
