from turtle import Turtle
from constants import *

# Attribute color to number or letter according to algorithm

class Selector():
    def __init__(self, screen):
        # Gets images for the arrows
        self.arrow_left = "assets/arrow_left_white.gif"
        self.arrow_right = "assets/arrow_right_white.gif"
        self.arrow_up = "assets/arrow_up_white30.gif"
        self.arrow_down = "assets/arrow_down_white.gif"
        # Makes images available for use
        screen.addshape(self.arrow_left)
        screen.addshape(self.arrow_right)
        screen.addshape(self.arrow_up)
        screen.addshape(self.arrow_down)

        self.rectangle = Turtle("square")
        self.rectangle.shapesize(stretch_len=RECTANGLE_LEN/SQUARE_DEFAULT_LEN, stretch_wid=RECTANGLE_WID/SQUARE_DEFAULT_LEN, outline=2)
        self.rectangle.penup()
        self.rectangle.color("black")
        self.rectangle.pencolor("white")
    
        self.rectangle_len = RECTANGLE_LEN
        self.rectangle_wid = RECTANGLE_WID

        # Sets possible positions for the selector rectangle and arrows
        # Index - Pos -> 0: Bottom, 1: Middle, 2: Top
        self.horizontal_pos = [
            [(0, -MOVE), (- self.rectangle_len/2 - REC_TO_ARROW_GAP - 25,  - MOVE), (self.rectangle_len/2 + REC_TO_ARROW_GAP + 25, -MOVE)],
            [(0, 0), (- self.rectangle_len/2 - REC_TO_ARROW_GAP - 25, 0), (self.rectangle_len/2 + REC_TO_ARROW_GAP + 25, 0)], 
            [(0, MOVE), (- self.rectangle_len/2 - REC_TO_ARROW_GAP - 25, MOVE), (self.rectangle_len/2 + REC_TO_ARROW_GAP + 25, MOVE)]
        ]

        # Sets possible positions for the selector rectangle and arrows
        # Index - Pos -> 0: Right, 1: Middle, 2: Left
        self.vertical_pos = [ 
            [(MOVE, 0), (MOVE, self.rectangle_len/2 + REC_TO_ARROW_GAP + 25), (MOVE, -self.rectangle_len/2 - REC_TO_ARROW_GAP - 25)],
            [(0, 0), (0, self.rectangle_len/2 + REC_TO_ARROW_GAP + 25), (0, -self.rectangle_len/2 - REC_TO_ARROW_GAP - 25)],
            [(-MOVE, 0), (-MOVE, self.rectangle_len/2 + REC_TO_ARROW_GAP + 25), (-MOVE, -self.rectangle_len/2 - REC_TO_ARROW_GAP - 25)]
        ]
        
        # Move rectangle to default position
        self.rectangle.setpos(self.horizontal_pos[1][0])

        # Creates arrow objects and sets them to default position
        self.left_select = Turtle()
        self.left_select.shape(self.arrow_up)
        self.left_select.penup()
        self.left_select.setpos(self.horizontal_pos[1][1])

        self.right_select = Turtle()
        self.right_select.shape(self.arrow_down)
        self.right_select.penup()
        self.right_select.setpos(self.horizontal_pos[1][2])

        # Adds selector items to list for easier object iteration
        self.selector_items = [self.rectangle, self.left_select, self.right_select]
        self.selector_pos = 1

    def rotate(self):
        """
        Rotates selector in-place by 90 degrees 
        """
        for index,item in enumerate(self.selector_items):
            # Check current selector orientation
            if item.heading()==0:
                # Rotate
                item.setheading(90)
                # Change to vertical position
                item.setpos(self.vertical_pos[self.selector_pos][index])
                # Change arrow orientation
                # Done using different images, not by changing heading - Turtle problem
                if index==1:
                    item.shape(self.arrow_left)
                elif index==2:
                    item.shape(self.arrow_right)
            else:
                # Rotate
                item.setheading(0)  
                # Change to horizontal position
                item.setpos(self.horizontal_pos[self.selector_pos][index])
                # Change arrow orientation
                # Done using different images, not by changing heading - Turtle problem
                if index==1:
                    item.shape(self.arrow_up)
                elif index==2:
                    item.shape(self.arrow_down)

    def move_up(self):
        """
        Moves selector one position up on the cube face
        """
        # Disable movement for max up position and for vertical mode
        if self.rectangle.pos() == self.horizontal_pos[2][0] or self.rectangle.heading()==90 :
            pass
        else:
            self.selector_pos += 1  
            # Move selector objects
            for index, item in enumerate(self.selector_items):
                item.setpos(self.horizontal_pos[self.selector_pos][index])

    def move_down(self):
        """
        Moves selector one position down on the cube face
        """
        # Disable movement for max down position and for vertical mode
        if self.rectangle.pos() == self.horizontal_pos[0][0] or self.rectangle.heading()==90 :
            pass
        else:
            self.selector_pos -= 1  
            # Set new position for each item
            for index, item in enumerate(self.selector_items):
                item.setpos(self.horizontal_pos[self.selector_pos][index])



    def move_left(self):
        """
        Moves selector one position left on the cube face
        """
        # Disable movement for max left position and for horizontal mode
        if self.rectangle.pos() == self.vertical_pos[2][0] or self.rectangle.heading()==0 :
            pass
        else:
            self.selector_pos += 1  
            # Set new position for each item
            for index, item in enumerate(self.selector_items):
                item.setpos(self.vertical_pos[self.selector_pos][index])

    def move_right(self):
        """
        Moves selector one position right on the cube face
        """
        # Disable movement for max right position and for horizontal mode
        if self.rectangle.pos() == self.vertical_pos[0][0] or self.rectangle.heading()==0 :
            pass
        else:
            self.selector_pos -= 1  
            # Set new position for each item
            for index, item in enumerate(self.selector_items):
                item.setpos(self.vertical_pos[self.selector_pos][index])       


