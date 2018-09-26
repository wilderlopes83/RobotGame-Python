import point

class Reward(point.Point):
    def __init__(self, x, y, name):
        super(Reward, self).__init__(x, y)
        self.name = name