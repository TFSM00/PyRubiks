import random as rnd
import pprint as pp
from square import Square


class Cube:
    def __init__(self):
        self.sides = ["F", "L", "R", "U", "D", "B"]
        self.cols = ["red", "white", "green", "blue", "orange", "yellow"]
        self.colors = {col: 8 for col in self.cols}
        self.cube = {side: [] for side in self.sides}
        self.horizontal_adjacents = ["F", "R", "B", "L"]
        self.vertical_adjacents = ["F", "U", "B", "D"]
        self.squares = []
        self.desig = {"F": "Front", "L": "Left", "R": "Right",
                      "U": "Top", "D": "Bottom", "B": "Back"}
        self.current_face = "F"
        self.current_horizontal_dir = 0  # 0 represents "right", 1 represents "up", 2 represents "left", 3 represents "down"
        self.current_vertical_dir = 0

    def set_face(self, face_desig: str):
        """
        Creates the squares for the Turtle Window
        """
        face = self.cube[face_desig]
        for row_index in range(3):
            row = []
            for col_index in range(3):
                square = Square(face[row_index][col_index])
                square.move_to_pos(row_index, col_index)
                row.append(square)
            self.squares.append(row)
        self.current_face = face_desig
        print(face)

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

    def populate_faces(self) -> None:
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

    # def rotate(self, side: str, screentext: object) -> None:
    #     match side:
    #         case "right":
    #             next_face_idx = abs(self.horizontal_adjacents.index(self.current_face) + 1) % \
    #                             len(self.horizontal_adjacents) # noqa
    #             next_face = self.horizontal_adjacents[next_face_idx]
    #         case "left":
    #             next_face_idx = abs(self.horizontal_adjacents.index(self.current_face) - 1) % \
    #                             len(self.horizontal_adjacents) # noqa
    #             next_face = self.horizontal_adjacents[next_face_idx]
    #         case "up":
    #             next_face_idx = abs(self.vertical_adjacents.index(self.current_face) + 1) % \
    #                             len(self.vertical_adjacents) # noqa
    #             next_face = self.vertical_adjacents[next_face_idx]
    #         case "down":
    #             next_face_idx = abs(self.vertical_adjacents.index(self.current_face) - 1) % \
    #                             len(self.vertical_adjacents) # noqa
    #             next_face = self.vertical_adjacents[next_face_idx]

    #     self.set_face(next_face)  # Update the current face
    #     screentext.update(self)
    def rotate(self, side: str, screentext: object) -> None:
        self.set_face(side)
        screentext.update(self)



if __name__ == "__main__":
    cube = Cube()
    cube.populate()
    pp.pprint(cube.cube)
