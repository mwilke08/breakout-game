import turtle

class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.shape('circle')
        self.ball.color('white')
        self.ball.setpos((0, 0))
        self.ball.shapesize(stretch_wid=.75, stretch_len=.75)
        self.game_on = False
        self.ball.penup()

    def update(self, player):
        current_x = self.ball.xcor()
        current_y = self.ball.ycor()
        new_x = current_x - 2
        new_y = current_y - 2
        # self.write_debug(player)
        self.ball.setpos(x=new_x, y=new_y)
        if self.ball.xcor()-45 >= player.getx() and self.ball.ycor() < -235:
            print('collision')
            new_y = new_y*-1
            new_x = new_x*-.75
            self.ball.setpos(x=new_x, y=new_y)

        if self.ball.xcor() < -295 or self.ball.xcor() > 295:
            new_x = new_x * -.75
            self.ball.setpos(x=new_x, y=self.ball.ycor())

        if self.ball.ycor() < -240 or self.ball.ycor() > 280:
            new_y = new_y *-1
            self.ball.setpos(x=self.ball.xcor(), y = new_y)




    def add_movement(self):
        current_x = self.ball.xcor()
        current_y = self.ball.ycor()
        new_x = current_x-1
        new_y = current_y-1
        self.ball.setpos(x=new_x, y=new_y)

    def toggle_game(self):
        if self.game_on:
            self.game_on = False
        else:
            self.game_on = True
            self.add_movement()

    def get_game_status(self):
        return self.game_on

    def write_debug(self, player):
        turtle.hideturtle()
        turtle.clear()
        # text_write = f"Player X: {player.getx()}, Player Y: {player.gety()}"
        # turtle.color("white")
        # turtle.setpos((0, 0))
        # turtle.write(text_write, font=("Arial", 8, "normal"))
        text_write = f"Ball X: {self.ball.xcor()}, Ball Y: {self.ball.ycor()}"
        turtle.setpos((0,40))
        turtle.color("white")
        turtle.write(text_write, font=("Arial", 8, "normal"))

    def check_collision(self, player_x, player_y):
        pass

    def getx(self):
        return self.getx()

    def gety(self):
        return self.gety()
