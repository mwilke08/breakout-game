import turtle

class Window:
    def __init__(self):
        self.window = turtle.Screen()

    def create_window(self):
        self.window = turtle.Screen()
        self.window.setup(width=600, height=600)
        self.window.bgcolor('gray')
        self.window.title("Breakout Game")
        self.window.colormode(255)

    def start_listening(self, player):
        self.window.listen()
        self.window.onkeypress(player.move_player_left, 'Left')
        self.window.onkeypress(player.move_player_right, 'Right')

    def get_window_height(self):
        return self.window.window_height()

    def get_window_width(self):
        return self.window.window_width()

    def print_debug(self, player, ball):
        turtle.hideturtle()
        text_write = f"Player X: {player.getx()}:Ball X: {ball.getx()}, Player Y: {player.gety()}:Ball Y: {ball.gety()}"
        turtle.write(text_write)

    def start_loop(self):
        self.window.mainloop()
