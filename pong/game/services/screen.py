import turtle

class Screen:
    """
    Creates the screen.
    """
    def __init__(self):
        pass

    def create_screen():
        sc = turtle.Screen()
        sc.title("Pong game")
        sc.bgcolor("white")
        sc.setup(width=1000, height=600)
        return sc