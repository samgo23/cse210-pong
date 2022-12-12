from game.casting.paddle import Paddle
from constants import *




class MovePaddle(Paddle):
    """
    Moves the paddles.
    """
    def __init__(self):
        super().__init__()
        
         

    def paddleaup(left_pad):
        y = left_pad.ycor()
        y += 20
        left_pad.sety(y)
        print('yes')
        return left_pad


    def paddleadown(left_pad):
        y = left_pad.ycor()
        y -= 20
        left_pad.sety(y)
        print('yes')
        return left_pad


    def paddlebup(right_pad):
        y = right_pad.ycor()
        y += 20
        right_pad.sety(y)
        print('yes')
        return right_pad


    def paddlebdown(right_pad):
        y = right_pad.ycor()
        y -= 20
        right_pad.sety(y)
        print('yes')
        return right_pad