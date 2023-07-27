from turtle import Turtle
from constants import *

class ScreenText():
    HEADER_FONT = ("Arial", 20, "bold")
    AUTHOR_FONT = ("Arial", 13, "normal")
    TEXT_FONT = ("Arial", 14, "normal")
    COPYRIGHT_FONT = ("Arial", 12, "normal")

    def __init__(self, cube):
        #TODO Maybe 1 turtle writes everything?
        self.objects = {"header": Turtle(), "author": Turtle(), "copyright": Turtle(), "current_face": Turtle(), "face": Turtle(), "hotkeys":Turtle()}

        for item in list(self.objects.values()):
            item.hideturtle()
            item.penup()
            item.color("white")
        
        self.objects["header"].setpos(0, SCREEN_HEIGHT/2 - self.HEADER_FONT[1] * 2)
        self.objects["header"].write("Rubik's Cube in Python", align="center", font=self.HEADER_FONT)

        self.objects["author"].setpos(0, self.objects["header"].pos()[1] - self.AUTHOR_FONT[1] * 2)
        self.objects["author"].write("Made by Tiago Moreira", align="center", font=self.AUTHOR_FONT)

        self.objects["copyright"].setpos(0, self.objects["author"].pos()[1] - self.AUTHOR_FONT[1] * 2)
        self.objects["copyright"].write("Copyright © 2023, TFSM00", align="center", font=self.COPYRIGHT_FONT)

        self.objects["hotkeys"].setpos(0, - SCREEN_HEIGHT/2 + self.TEXT_FONT[1] * 2)
        self.objects["hotkeys"].write("Hotkeys Here!", align="center", font=self.TEXT_FONT)

        self.objects["face"].setpos(0, self.objects["hotkeys"].pos()[1] + self.TEXT_FONT[1] * 4)
        self.objects["face"].write(f"{cube.current_face}: {cube.designations[cube.current_face]}", align="center", font=self.TEXT_FONT)

        self.objects["current_face"].setpos(0, self.objects["face"].pos()[1] + self.TEXT_FONT[1] * 2)
        self.objects["current_face"].write("Current Face", align="center", font=self.TEXT_FONT)
        