class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2
triangulo = Triangulo(10, 5)
print(triangulo.calcular_area())