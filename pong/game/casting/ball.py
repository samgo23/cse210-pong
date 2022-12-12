import turtle

class Ball:
    "A ball that bounces of the paddles"

    def __init__(self):
        pass

    def construct_ball():
        # Ball of circle shape
        hit_ball = turtle.Turtle()
        hit_ball.speed(40)
        hit_ball.shape("circle")
        hit_ball.color("blue")
        hit_ball.penup()
        hit_ball.goto(0, 0)
        hit_ball.dx = 5
        hit_ball.dy = -5
        return hit_ball