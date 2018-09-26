import point

class Robot(point.Point):
    def __init__(self, x, y):
        super(Robot, self).__init__(x, y)

    def move_up(self):
        if (self.y) < 10:
            self.y += 1
        else:
            print('Movimento inválido')

    def move_down(self):
        if (self.y) > 0:
            self.y -= 1
        else:
            print('Movimento inválido')            

    def move_left(self):
        if (self.x) > 0:
            self.x -= 1
        else:
            print('Movimento inválido')                        

    def move_right(self):
        if (self.x) < 10:
            self.x += 1
        else:
            print('Movimento inválido')
