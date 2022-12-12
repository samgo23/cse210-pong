from game.casting.actor import Actor
from constants import *
import turtle

class Paddle(Actor):
    """
    A solid rectangle object that hits the ball
    """
    def __init__(self):
        """
    
        """
        pass

    def build_paddle(side, player):
        """
        Creates the paddles.
        """
        side = turtle.Turtle()
        side.shape("square")
        side.speed(0)
        side.color("black")
        side.shapesize(stretch_wid=6, stretch_len=2)
        side.penup()
        if player == left:
            side.goto(-400, 0)
        else:
            side.goto(400, 0)
        return side