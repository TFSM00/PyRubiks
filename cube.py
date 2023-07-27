import random as rnd
import pprint as pp
from square import Square
from constants import *

class Cube:
    def __init__(self):     
        self.sides = ["F", "L", "R", "U", "D", "B"]
        self.cols = ["red", "white", "green", "blue", "orange", "yellow"]
        self.colors = {col: 8 for col in self.cols}
        self.cube = {side: [] for side in self.sides}
        self.horizontal_adjacents = ["L", "F", "F", "B"]
        self.vertical_adjacents = ["U", "F", "D", "B"]
        self.squares = []
        self.designations = {"F": "Front", "L": "Left", "R": "Right", "U": "Top", "D": "Bottom", "B": "Back"}
        self.current_face = "F"

    def set_face(self):
        """
        Creates the squares for the Turtle Window
        """
        self.populate()
        front_face = self.cube["F"]
        for row_index in range(3):
            row = []
            for col_index in range(3):
                square = Square(front_face[row_index][col_index])
                square.move_to_pos(row_index, col_index)
                row.append(square)
            self.squares.append(row)
        print(self.cube["F"])

    def populate(self):
        """
        Fills cube faces
        """
        self.zero_populate()
        self.populate_middle()
        self.populate_faces()

    def zero_populate(self):
        """
        Fills cube dict with zeroes
        """
        for side in self.sides:
            for _ in range(3):
                self.cube[side].append([0, 0, 0])

    def populate_middle(self):
        """
        Fills cube center squares with each color
        """
        center_cols = self.cols
        for side in self.sides:
            chosen_color = rnd.choice(center_cols)
            self.cube[side][1][1] = chosen_color
            center_cols.pop(center_cols.index(chosen_color))
    
    def populate_faces(self):
        """
        Fills zero filled cubes with a random color
        """
        for side in self.sides:
            for row in range(3):
                for square in range(3):
                    if self.cube[side][row][square] == 0:
                        col = rnd.choice(list(self.colors.keys()))
                        while self.colors[col] == 0:
                            col = rnd.choice(list(self.colors.keys()))
                        self.colors[col] = self.colors[col] - 1
                        self.cube[side][row][square] = col


if __name__=="__main__":
    cube = Cube()
    cube.populate()
    pp.pprint(cube.cube)    



# Populate centers


# print(cube)