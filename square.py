from turtle import Turtle
from constants import *

class Square(Turtle):
    def __init__(self, color):
        super().__init__()
        self.color(color)
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=SQUARE_SIZE/SQUARE_DEFAULT_LEN, 
                       stretch_wid=SQUARE_SIZE/SQUARE_DEFAULT_LEN, 
                       outline=2)
        # Might need to change positions so center is [y][0] instead
        self.positions = [
            [(- SQUARE_SIZE - GAP, SQUARE_SIZE + GAP), (0, SQUARE_SIZE + GAP), (SQUARE_SIZE + GAP, SQUARE_SIZE + GAP)],
            [(- SQUARE_SIZE - GAP, 0), (0, 0), (SQUARE_SIZE + GAP, 0)],
            [(- SQUARE_SIZE - GAP, - SQUARE_SIZE - GAP), (0, - SQUARE_SIZE - GAP), (SQUARE_SIZE + GAP, - SQUARE_SIZE - GAP)]
        ]
        

    def move_to_pos(self, row_index, col_index):
        self.setpos(self.positions[row_index][col_index])

        
