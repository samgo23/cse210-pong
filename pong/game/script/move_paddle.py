from game.casting.paddle import Paddle
from constants import *




class MovePaddle(Paddle):
    """
    Moves the paddles.
    """
    def __init__(self):
        super().__init__()

        self.left_pad = 0
        self.right_pad = 0
         

    def paddleaup(self):
        y = self.left_pad.ycor()
        y += 20
        self.left_pad.sety(y)
        return self.left_pad


    def paddleadown(self):
        y = self.left_pad.ycor()
        y -= 20
        self.left_pad.sety(y)
        return self.left_pad


    def paddlebup(self):
        y = self.right_pad.ycor()
        y += 20
        self.right_pad.sety(y)
        return self.right_pad


    def paddlebdown(self):
        y = self.right_pad.ycor()
        y -= 20
        self.right_pad.sety(y)
        return self.right_pad