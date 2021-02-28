def on_button_pressed_a():
    if PaddleA.get(LedSpriteProperty.X) > 0:
        PaddleA.change(LedSpriteProperty.X, -1)
        PaddleB.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if PaddleB.get(LedSpriteProperty.X) < 4:
        PaddleA.change(LedSpriteProperty.X, 1)
        PaddleB.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

PaddleB: game.LedSprite = None
PaddleA: game.LedSprite = None
PaddleA = game.create_sprite(2, 4)
PaddleB = game.create_sprite(3, 4)
ball = game.create_sprite(randint(0, 4), 0)
directionY = 1
directionX = randint(-1, 1)
basic.pause(500)

def on_forever():
    global directionY, directionX
    ball.change(LedSpriteProperty.X, directionX)
    ball.change(LedSpriteProperty.Y, directionY)
    if ball.is_touching(PaddleA) or ball.is_touching(PaddleB):
        ball.change(LedSpriteProperty.X, directionX)
        ball.change(LedSpriteProperty.Y, -1)
        directionY = -1
        directionX = randint(-1, 1)
    basic.pause(1000)
basic.forever(on_forever)
