from turtle import Turtle
from constants import *

# Attribute color to number or letter according to algorithm

class Selector():
    def __init__(self, screen):
        # Make image path constant
        arrow_left = "arrow_left_white.gif"
        arrow_right = "arrow_right_white.gif"
        screen.addshape(arrow_left)
        screen.addshape(arrow_right)

        self.rectangle = Turtle("square")
        self.rectangle.shapesize(stretch_len=RECTANGLE_LEN/SQUARE_DEFAULT_LEN, stretch_wid=RECTANGLE_WID/SQUARE_DEFAULT_LEN, outline=2)
        self.rectangle.penup()
        self.rectangle.color("black")
        self.rectangle.pencolor("white")
    

        self.rectangle_len = RECTANGLE_LEN
        self.rectangle_wid = RECTANGLE_WID

        self.horizontal_pos = [
            [(0, -MOVE), (- self.rectangle_len/2 - REC_TO_ARROW_GAP - 25,  - MOVE), (self.rectangle_len/2 + REC_TO_ARROW_GAP + 25, -MOVE)],
            [(0, 0), (- self.rectangle_len/2 - REC_TO_ARROW_GAP - 25, 0), (self.rectangle_len/2 + REC_TO_ARROW_GAP + 25, 0)], 
            [(0, MOVE), (- self.rectangle_len/2 - REC_TO_ARROW_GAP - 25, MOVE), (self.rectangle_len/2 + REC_TO_ARROW_GAP + 25, MOVE)]
        ]

        self.vertical_pos = [ 
            [(MOVE, 0), (MOVE, self.rectangle_len/2 + REC_TO_ARROW_GAP + 25), (MOVE, -self.rectangle_len/2 - REC_TO_ARROW_GAP - 25)],
            [(0, 0), (0, self.rectangle_len/2 + REC_TO_ARROW_GAP + 25), (0, -self.rectangle_len/2 - REC_TO_ARROW_GAP - 25)],
            [(-MOVE, 0), (-MOVE, self.rectangle_len/2 + REC_TO_ARROW_GAP + 25), (-MOVE, -self.rectangle_len/2 - REC_TO_ARROW_GAP - 25)]
        ]
        
        self.rectangle.setpos(self.horizontal_pos[1][0])

        self.left_select = Turtle()
        self.left_select.shape(arrow_left)
        self.left_select.penup()
        self.left_select.setpos(self.horizontal_pos[1][1])

        self.right_select = Turtle()
        self.right_select.shape(arrow_right)
        self.right_select.penup()
        self.right_select.setpos(self.horizontal_pos[1][2])

        self.selector_items = [self.rectangle, self.left_select, self.right_select]
        self.selector_pos = 1

        #TODO: Turn everything 90 on rotation

    def move_up(self):
        if self.rectangle.pos() == self.horizontal_pos[2][0]:
            pass
        else:
            self.selector_pos += 1  
            for index, item in enumerate(self.selector_items):
                item.setpos(self.horizontal_pos[self.selector_pos][index])

    def move_down(self):
        if self.rectangle.pos() == self.horizontal_pos[0][0]:
            pass
        else:
            self.selector_pos -= 1  
            for index, item in enumerate(self.selector_items):
                item.setpos(self.horizontal_pos[self.selector_pos][index])

                    


