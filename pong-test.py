# Import required library
import turtle
from constants import *

padheight = stretch_wid=6
padlength = stretch_len=2

# Create screen
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

class Actor:
    """A thing that participates in the game."""
    
    def __init__(self, debug = False):
        """Constructs a new Actor using the given group and id.
        
        Args:
            group: A string containing the actor's group name.
            id: A number that uniquely identifies the actor within the group.
        """
        self._debug = debug
        
    def is_debug(self):
        """Whether or not the actor is being debugged.
        
        Returns:
            True if the actor is being debugged; False if otherwise.
        """
        return self._debug




class Paddle(Actor): 

	def __init__(self): 
		"""
		
		"""
	def draw_paddle(self):
		
		self.pad = turtle.Turtle()
		self.pad.speed(0)
		self.pad.shape("square")
		self.pad.color("black")
		self.pad.shapesize(padheight, padlength)
		self.pad.penup()
		left_pad = self.pad.goto(LEFT, 0)
		right_pad = self.pad.goto(RIGHT, 0)
		return left_pad, right_pad


Paddle.draw_paddle


# Ball of circle shape
class Ball(Actor):
    "A paddle in the game"

    def __init__(self, debug=False):
        """Constructs a new Ball.

            Args:
                body: A new instance of Body.
                image: A new instance of Image.
                debug: If it is being debugged. 
        """
        super().__init__(debug)

hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5


# Initialize the score
left_player = 0
right_player = 0


# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0 Right_player: 0",
			align="center", font=("Courier", 24, "normal"))


# Functions to move paddle vertically
class MovePaddle:

	def paddleaup(self, side):
		y = side.pad.ycor()
		y += 20
		side.pad.sety(y)


	def paddleadown(self, side):
		y = side.pad.ycor()
		y -= 20
		side.pad.sety(y)



# Keyboard bindings
class KeyboardService:
    """A keyboard service inteface."""

    def is_key_down(self, key):
        """Detects if the given key is being pressed.
        
        Args:
            key: A string containing the key value, e.g. 'a', '0', etc.

        Returns:
            True if the key is being pressed; false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_key_pressed(self, key):
        """Detects if the given key was pressed once.
        
        Args:
            key: A string containing the key value, e.g. 'a', '0', etc.

        Returns:
            True if the key was pressed once; false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_key_released(self, key):
        """Detects if the given key was released once.
        
        Args:
            key: A string containing the key value, e.g. 'a', '0', etc.

        Returns:
            True if the key was released once; false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_key_up(self, key):
        """Detects if the given key is released.
        
        Args:
            key: A string containing the key value, e.g. 'a', '0', etc.

        Returns:
            True if the key is released; false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")

sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")


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
		sketch.write("Left_player : {} Right_player: {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal"))

	if hit_ball.xcor() < -500:
		hit_ball.goto(0, 0)
		hit_ball.dy *= -1
		right_player += 1
		sketch.clear()
		sketch.write("Left_player : {} Right_player: {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal"))

	# Paddle ball collision
	if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() <= right_pad.ycor() + 500 and hit_ball.ycor() >= right_pad.ycor() - padheight):
		hit_ball.setx(360)
		hit_ball.dx*=-1
		
	if (hit_ball.xcor()< -360 and hit_ball.xcor()> -370) and (hit_ball.ycor() <= left_pad.ycor() + 100 and hit_ball.ycor() >= left_pad.ycor() - 100):
		hit_ball.setx(-360)
		hit_ball.dx*=-1
