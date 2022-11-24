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
        elif self.x < 0 and self.y < 0:
            print("{} Pertenece al tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} Pertenece al cuarto cuadrante".format(self))
        else:
            print("{} Se encuentra sobre el origen".format(self))

    def vectores(self, p):
        print("El vector entre {} y {} es ({}, {})".format(self, p, p.x - self.x, p.y - self.y))

    def distancia(self, p):
        d = math.sort( (p.x - self.x)**2 + (p.y - self.y)**2 )
        print("La distancia entre los puentos {} y {} es {}".format(self, p, d))

class rectangulo:
    def __init__(self,PInicial=Punto(), FFinal=Punto() ):
        self.PInicial = pInicial
        self.FFinal = fFinal

    def base(self):
        self.base = self.PFinal.x - self.PInicial.x
        print("La base del rectangulo es {}".format(self.base))

    def altura(self):
        self.altura = self.PFinal.y - self.PInicial.y
        print("La altura del rectangulo es {}".format(self.altura))

    def area(self):
        self.base = self.PFinal.x - self.PInicial.x
        self.altura = self.PFinal.y - self.PInicial.y
        self.area = self.base * self.altura
        print("El area del rectangulo es {}".format(self.area))
