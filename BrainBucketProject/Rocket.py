class Rocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move_up(self):
        print(self.y + 1)

    def move_right(self):
        print(self.x + 1)

    def move_down(self):
        print(self.y - 1)

    def move_left(self):
        print(self.x - 1)

    def current_position(self):
        print(self.x + self.y)


move1 = Rocket(0,0)
move1.move_up()

move2 = Rocket(0,0)
move2.move_right()

move3 = Rocket(0,0)
move3.move_down()

move4 = Rocket(0,0)
move4.move_left()

current = Rocket(0,0)
current.current_position()

