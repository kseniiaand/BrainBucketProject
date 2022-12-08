class Rocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move_up(self):
        self.y += 1
        print(self.y)

    def move_right(self):
        self.x += 1
        print(self.x)

    def move_down(self):
        self.y -= 1
        print(self.y)


    def move_left(self):
        self.x -= 1
        print(self.x)

    def current_position(self):
        print(self.x, self.y)


Rocket1 = Rocket(0,0)
Rocket1.move_up()
Rocket1.move_right()
Rocket1.move_left()
Rocket1.move_down()
Rocket1.current_position()

