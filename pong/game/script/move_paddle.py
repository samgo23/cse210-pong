from game.casting.paddle import Paddle
from constants import *




class MovePaddle(Paddle):
    """
    Moves the paddles.
    """
    def __init__(self):
        super().__init__()
        self.y = 0
        self.left_pad = 0
        self.right_pad = 0
         

    def paddleaup(self):
        self.y = self.left_pad.ycor()
        self.y += 20
        self.left_pad.sety(self.y)
        print('yes')
        return self.left_pad


    def paddleadown(self):
        self.y = self.left_pad.ycor()
        self.y -= 20
        self.left_pad.sety(self.y)
        print('yes')
        return self.left_pad


    def paddlebup(self):
        self.y = self.right_pad.ycor()
        self.y += 20
        self.right_pad.sety(self.y)
        print('yes')
        return self.right_pad


    def paddlebdown(self):
        self.y = self.right_pad.ycor()
        self.y -= 20
        self.right_pad.sety(self.y)
        print('yes')
        return self.right_pad