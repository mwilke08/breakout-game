from Player import Player
from Ball import Ball
from Window import Window
from Blocks import Blocks
import time

# init player class
player = Player()

# init window class
window = Window()
window.start_listening(player=player)
window.create_window()
player.start_game(x=0, y=-(window.get_window_height()/2-45))

# init ball class
ball = Ball()

# init blocks class
blocks = Blocks()
blocks.create_level_blocks()

ball.game_on = True
if __name__ == "__main__":
    ball.add_movement()
    while True:
        ball.update(player)
        time.sleep(.01)


