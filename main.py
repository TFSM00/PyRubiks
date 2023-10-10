from turtle import Screen
from cube import Cube
from selector import Selector
from screentext import ScreenText
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Rubik's Cube in Python")

selector = Selector(screen)
cube = Cube()
screentext = ScreenText(cube)


cube.populate()
cube.set_face("F")

screen.listen()
screen.onkey(selector.move_up, "Up")
screen.onkey(selector.move_down, "Down")
screen.onkey(selector.rotate, "r")
screen.onkey(selector.move_left, "Left")
screen.onkey(selector.move_right, "Right")
screen.onkey(lambda: cube.rotate("F", screentext), "1")
screen.onkey(lambda: cube.rotate("L", screentext), "2")
screen.onkey(lambda: cube.rotate("R", screentext), "3")
screen.onkey(lambda: cube.rotate("U", screentext), "4")
screen.onkey(lambda: cube.rotate("D", screentext), "5")
screen.onkey(lambda: cube.rotate("B", screentext), "6")

while True:
    screen.update()

screen.exitonclick()
