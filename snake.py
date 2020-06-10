import pygame as p
from random import randint
from enum import Enum

class Directions (Enum):                            ååøøææ
    RIGHT = (20, 0)
    LEFT = (-20, 0)
    UP = (0, -20)
    DOWN = (0, 20)
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property
    def getX(self):
        return self.x
    @property
    def getY(self):
        return self.y

screen = p.display.set_mode((700, 500))
clock = p.time.Clock()
play = True
length = 0
theFood = 0
direction = Directions.DOWN
snakeLength = 1
snake = [ [0, 0], [0, 20] ]

def removeTail () :
    while snakeLength < len( snake ) :
        a = snake[0][0]
        b = snake[0][1]
        draw(a, b, 0, 0, 0)
        snake.pop(0)

def move ():
    global snakeLength
    global theFood

    if not theFood:
        food()
    length = len(snake) - 1
    a = snake[length][0] + direction.getX
    b = snake[length][1] + direction.getY
    try:
        snake.index([a, b])
    except:
        snake.append([a, b])
        a = snake[length + 1][0]
        b = snake[length + 1][1]
        draw(a, b, 0, 255, 0)
        if snake[length + 1] == theFood:
            snakeLength += 1
            theFood = 0
    else:
        raise SystemExit

def getEvent () :
    global direction
    global play

    for event in p.event.get():
        if event.type == p.KEYDOWN and event.key == p.K_q:
            raise SystemExit
        if event.type == p.KEYDOWN and event.key == p.K_w:
            if direction != Directions.DOWN or len(snake) == 1:
                direction = Directions.UP
        if event.type == p.KEYDOWN and event.key == p.K_d:
            if direction != Directions.LEFT or len(snake) == 1:
                direction = Directions.RIGHT
        if event.type == p.KEYDOWN and event.key == p.K_s:
            if direction != Directions.UP or len(snake) == 1:
                direction = Directions.DOWN
        if event.type == p.KEYDOWN and event.key == p.K_a:
            if direction != Directions.RIGHT or len(snake) == 1:
                direction = Directions.LEFT

def draw (a, b, colour1, colour2, colour3):
    p.draw.rect(screen, (colour1, colour2, colour3), p.Rect(a, b, 18, 18))

def food ():
    global theFood

    while True:
        a = randint(0, 34) * 20
        b = randint(0, 24) * 20
        try:
            snake.index([a, b])
        except:
            draw(a, b, 255, 0, 0)
            theFood = [a, b]
            break

def death ():
    length = len(snake) - 1
    if snake[length][0] > 700 or snake[length][0] < 0:
        raise SystemExit
    if snake[length][1] > 500 or snake[length][1] < 0:
        raise SystemExit

while True:
    p.time.wait(100)
    getEvent()
    move()
    removeTail()
    death()
    
    p.display.flip()
    p.display.set_caption("Score: " + str(snakeLength - 1))
