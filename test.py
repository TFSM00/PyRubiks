class RubiksCube:
    def __init__(self):
        # Initialize the cube with each face represented by a 2D array
        self.front = [['F' for _ in range(3)] for _ in range(3)]
        self.back = [['B' for _ in range(3)] for _ in range(3)]
        self.up = [['U' for _ in range(3)] for _ in range(3)]
        self.down = [['D' for _ in range(3)] for _ in range(3)]
        self.left = [['L' for _ in range(3)] for _ in range(3)]
        self.right = [['R' for _ in range(3)] for _ in range(3)]

    def rotate_face(self, face):
        # Rotate a single face (clockwise)
        rotated_face = [list(row) for row in zip(*reversed(face))]
        return rotated_face

    def rotate(self, direction):
        # Define the rotation mappings
        rotation_mapping = {
            'up': (self.up, self.front, self.down, self.back, self.left, self.right),
            'down': (self.down, self.front, self.up, self.back, self.right, self.left),
            'left': (self.left, self.front, self.right, self.back, self.down, self.up),
            'right': (self.right, self.front, self.left, self.back, self.up, self.down)
        }

        if direction in rotation_mapping:
            to_rotate, front_face, back_face, up_face, down_face, left_face, right_face = rotation_mapping[direction]
            to_rotate[:] = self.rotate_face(to_rotate)
            # Update adjacent faces
            front_face[:] = self.rotate_face(front_face)
            back_face[:] = self.rotate_face(back_face)
            up_face[:] = self.rotate_face(up_face)
            down_face[:] = self.rotate_face(down_face)
            left_face[:] = self.rotate_face(left_face)
            right_face[:] = self.rotate_face(right_face)

    def __str__(self):
        # Display the current state of the cube
        cube_str = ""
        for face_name, face in [('Front', self.front), ('Back', self.back), ('Up', self.up),
                               ('Down', self.down), ('Left', self.left), ('Right', self.right)]:
            cube_str += face_name + ':\n'
            for row in face:
                cube_str += ' '.join(row) + '\n'
            cube_str += '\n'
        return cube_str

import os
# Example usage:
cube = RubiksCube()
print(cube)
os.system('clear')
cube.rotate('right')
print(cube)
os.system('clear')
cube.rotate('up')
print(cube)
os.system('clear')
cube.rotate('up')
print(cube)
