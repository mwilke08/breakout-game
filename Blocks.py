import turtle
import random

class Blocks:
    def __init__(self):
        self.all_blocks = []
        self.colors = ['green', 'yellow', 'blue', 'orange', 'red', 'skyblue', 'navy', 'purple', 'gold', 'darkgreen']

    def create_level_blocks(self):
        x_cor = -230
        y_cor = 280
        # create all the blocks for the level
        for i in range(28):
            block = turtle.Turtle()
            block.speed("fastest")
            block.shape("square")
            block.shapesize(stretch_len=3.5, stretch_wid=1)
            rand_color = random.choice(self.colors)
            block.color(rand_color)
            block.penup()
            if x_cor > (600 / 2) - 30:
                x_cor = -230
                y_cor -= 30
            block.setpos(x=x_cor, y=y_cor)
            x_cor += 75
            self.all_blocks.append(block)
