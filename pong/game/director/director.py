import turtle
from game.casting.paddle import Paddle
from game.services.screen import Screen
from game.casting.ball import Ball
from game.services.score import Score
from game.script.move_paddle import MovePaddle
from constants import *

class Director:
    
    def __init__(self):
        self.sc = Screen.create_screen()
        self.left_pad = ''
        self.right_pad = ''
        self.hit_ball = ''
        self.left_player = ''
        self.right_player = ''
        self.sketch = ''

        self._move_paddle = MovePaddle()

    def start_game(self):
        """
        Starts a new game.
        """
        
        while True:
            self.get_inputs()
            self.do_updates()

    def get_inputs(self):
        """
        
        """
        
        self.sc.listen()
        self.sc.onkeypress(self._move_paddle.paddleaup, "w")
        self.sc.onkeypress(self._move_paddle.paddleadown, "s")
        self.sc.onkeypress(self._move_paddle.paddlebup, "Up")
        self.sc.onkeypress(self._move_paddle.paddlebdown, "Down")

        self.left_pad = Paddle.build_paddle(left, left)
        self.right_pad = Paddle.build_paddle(right, right) 

        self.hit_ball = Ball.construct_ball()

        self.left_player = Score.player_score(left)
        self.right_player = Score.player_score(right)
        self.sketch = Score.display_score()


    def do_updates(self):
        """
        
        """
        while True:
            self.sc.update()

            self.hit_ball.setx(self.hit_ball.xcor()+ self.hit_ball.dx)
            self.hit_ball.sety(self.hit_ball.ycor()+ self.hit_ball.dy)

            # Checking borders
            if self.hit_ball.ycor() > 280:
                self.hit_ball.sety(280)
                self.hit_ball.dy *= -1

            if self.hit_ball.ycor() < -280:
                self.hit_ball.sety(-280)
                self.hit_ball.dy *= -1

            if self.hit_ball.xcor() > 500:
                self.hit_ball.goto(0, 0)
                self.hit_ball.dy *= -1
                self.left_player += 1
                self.sketch.clear()
                self.sketch.write("Left Player : {} Right Player: {}".format(self.left_player, self.right_player), align="center", font=("Courier", 24, "normal"))

            if self.hit_ball.xcor() < -500:
                self.hit_ball.goto(0, 0)
                self.hit_ball.dy *= -1
                self.right_player += 1
                self.sketch.clear()
                self.sketch.write("Left Player : {} Right Player: {}".format(self.left_player, self.right_player), align="center", font=("Courier", 24, "normal"))

            # Paddle ball collision
            if (self.hit_ball.xcor() > 360 and self.hit_ball.xcor() < 370) and (self.hit_ball.ycor() < self.right_pad.ycor() + COLLISION_AREA and self.hit_ball.ycor() > self.right_pad.ycor() - COLLISION_AREA):
                self.hit_ball.setx(360)
                self.hit_ball.dx*=-1
                
            if (self.hit_ball.xcor()<-360 and self.hit_ball.xcor()>-370) and (self.hit_ball.ycor()< self.left_pad.ycor() + COLLISION_AREA and self.hit_ball.ycor() > self.left_pad.ycor() - COLLISION_AREA):
                self.hit_ball.setx(-360)
                self.hit_ball.dx*=-1
