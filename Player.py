import turtle

MOVE_SPEED = 15

class Player:
    def __init__(self):
        self.player = turtle.Turtle()
        self.player.penup()
        self.player.shape('square')
        self.player.speed("fastest")
        self.player.shapesize(stretch_wid=.5, stretch_len=5)
        self.game_on = False

    def start_game(self, x, y):
        self.game_on = True
        self.reset_player(x, y)
        self.player.showturtle()

    def reset_player(self, x, y):
        self.player.goto(x=x, y=y)

    def move_player_right(self):
        current_x = self.player.xcor()
        self.player.setx(current_x+MOVE_SPEED)

    def move_player_left(self):
        current_x = self.player.xcor()
        self.player.setx(current_x-MOVE_SPEED)

    def check_collision(self, ballx, bally):
        print('in collision check')
        player_x = self.getx()
        player_y = self.gety()
        if ballx == player_x and bally <= player_y:
            print("collision")

    def get_game_status(self):
        return self.game_on

    def getx(self):
        return self.player.xcor()

    def gety(self):
        return self.player.xcor()

