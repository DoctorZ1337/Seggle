from ball import Ball
from peg import Peg

balls = []
pegs = []

def update_balls():
    for i in range(len(balls) - 1, -1, -1):
        balls[i].update()
        if not balls[i].alive:
            balls.pop(i)
    for i in range(len(pegs) - 1, -1, -1):
        if not pegs[i].alive:
            pegs.pop(i)

def draw_balls():
    for i in range(len(balls)):
        balls[i].draw()

def draw_pegs():
    for peg in pegs:
        peg.draw()