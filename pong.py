# Import required library
import turtle
from pong.game.casting.paddle import Paddle
from pong.game.services.screen import Screen
from pong.game.casting.ball import Ball
from pong.game.services.score import Score
from pong.game.script.move_paddle import MovePaddle
from pong.constants import *


    

    


left_pad = Paddle.build_paddle(left, left)
right_pad = Paddle.build_paddle(right, right) 

hit_ball = Ball.construct_ball()

left_player = Score.player_score(left)
right_player = Score.player_score(right)
sketch = Score.display_score()



sc = Screen.create_screen()

# Keyboard bindings
sc.listen()
sc.onkeypress(MovePaddle.paddleaup, "w")
sc.onkeypress(MovePaddle.paddleadown, "s")
sc.onkeypress(MovePaddle.paddlebup, "Up")
sc.onkeypress(MovePaddle.paddlebdown, "Down")

class Director:
    
    def __init__(self) -> None:
        pass

    def start_game():
        """
        Starts a new game.
        """
        while True:
            Director.get_inputs()
            Director.do_updates()

    def get_inputs():
        """
        
        """
        sc.listen()
        sc.onkeypress(MovePaddle.paddleaup, "w")
        sc.onkeypress(MovePaddle.paddleadown, "s")
        sc.onkeypress(MovePaddle.paddlebup, "Up")
        sc.onkeypress(MovePaddle.paddlebdown, "Down")

    def do_updates():
        """
        
        """
class Borders:
    """
    
    """
    def __init__(self) -> None:
        pass

    def check_borders():
        """
        
        """
        pass


while True:
	sc.update()

	hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
	hit_ball.sety(hit_ball.ycor()+hit_ball.dy)

	# Checking borders
	if hit_ball.ycor() > 280:
		hit_ball.sety(280)
		hit_ball.dy *= -1

	if hit_ball.ycor() < -280:
		hit_ball.sety(-280)
		hit_ball.dy *= -1

	if hit_ball.xcor() > 500:
		hit_ball.goto(0, 0)
		hit_ball.dy *= -1
		left_player += 1
		sketch.clear()
		sketch.write("Left Player : {} Right Player: {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal"))

	if hit_ball.xcor() < -500:
		hit_ball.goto(0, 0)
		hit_ball.dy *= -1
		right_player += 1
		sketch.clear()
		sketch.write("Left Player : {} Right Player: {}".format(
								left_player, right_player), align="center",
								font=("Courier", 24, "normal"))

	# Paddle ball collision
	if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor() + COLLISION_AREA and hit_ball.ycor() > right_pad.ycor() - COLLISION_AREA):
		hit_ball.setx(360)
		hit_ball.dx*=-1
		
	if (hit_ball.xcor()<-360 and hit_ball.xcor()>-370) and (hit_ball.ycor()<left_pad.ycor() + COLLISION_AREA and hit_ball.ycor() > left_pad.ycor() - COLLISION_AREA):
		hit_ball.setx(-360)
		hit_ball.dx*=-1
