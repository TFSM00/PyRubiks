from turtle import Screen
from cube import Cube
from selector import Selector
from screentext import ScreenText
from constants import *

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Rubik's Cube in Python")

selector = Selector(screen)
cube = Cube()
screentext = ScreenText(cube)


cube.set_face()

screen.listen()
screen.onkey(selector.move_up, "Up")
screen.onkey(selector.move_down, "Down")
screen.onkey(selector.rotate, "r")
screen.onkey(selector.move_left, "Left")
screen.onkey(selector.move_right, "Right")

while True:
    screen.update()

screen.exitonclick()
