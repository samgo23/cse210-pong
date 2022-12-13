import turtle

class Score:
    "player scores"

    def __init__(self) -> None:
        pass

    def player_score(player):
        """Initialize the score"""
        player = 0
        return player 

    def display_score():
        """
        Displays score on to the screen.
        """
        # Displays the score
        sketch = turtle.Turtle()
        sketch.speed(0)
        sketch.color("blue")
        sketch.penup()
        sketch.hideturtle()
        sketch.goto(0, 260)
        sketch.write("Left_player : 0 Right_player: 0", align="center", font=("Courier", 24, "normal"))
        return sketch