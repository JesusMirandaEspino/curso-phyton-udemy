import math

class punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} Pertenece al primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} Pertenece al segundo cuadrante".format(self))
    