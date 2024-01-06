from abc import ABC, abstractmethod
import numpy as np


class Figura(ABC):
    def __init__(self, area, circuit):
        self.area = area
        self.circuit = circuit

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def figure(self):
        pass

    def przedstaw_sie(self):
        print(f"Jestem {self.figure()} moja powierzchnia to {self.area()}, a obwód {self.circuit()}cm.")


class Circle(Figura):
    def __init__(self, r):
        self.r = r

    def area(self):
        area = np.pi * self.r * self.r
        return area

    def circuit(self):
        circuit = 2 * np.pi * self.r
        return circuit

    def figure(self):
        return "KOŁO"


class Rectangle(Figura):
    def __init__(self, a, b):
        self.b = b
        self.a = a

    def area(self):
        area = self.a * self.b
        return area

    def circuit(self):
        circuit = 2 * (self.a + self.b)
        return circuit

    def figure(self):
        return "PROSTOKĄT"


class Square(Figura):
    def __init__(self, a):
        self.a = a

    def area(self):
        area = self.a * self.a
        return area

    def circuit(self):
        circuit = 4 * self.a
        return circuit

    def figure(self):
        return "KWADRAT"


class Triangle(Figura):
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def area(self):
        area = (self.a * self.h)/2
        return area

    def circuit(self):
        circuit = self.a + 2 * ((self.a/2) ** 2 + self.h ** 2) ** 0.5
        return circuit

    def figure(self):
        return "TRÓJKĄT"

fig1 = Circle(3)
fig2 = Rectangle(3,4)
fig3 = Square(2)
fig4 = Triangle(6,2)

fig1.przedstaw_sie()
fig2.przedstaw_sie()
fig3.przedstaw_sie()
fig4.przedstaw_sie()