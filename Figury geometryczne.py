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
    def __init__(self, a, b, c):
        self.c = c
        self.b = b
        self.a = a

    def area(self):
        p = (self.a + self.b + self.c)/2
        area = np.sqrt(p*(p - self.a)*(p - self.b)*(p - self.c))
        return area

    def circuit(self):
        circuit = self.a + self.b + self.c
        return circuit

    def figure(self):
        return "TRÓJKĄT"


def main():
    fig1 = Circle(3)
    fig2 = Rectangle(3, 4)
    fig3 = Square(2)
    fig4 = Triangle(4, 5, 7)

    fig1.przedstaw_sie()
    fig2.przedstaw_sie()
    fig3.przedstaw_sie()
    fig4.przedstaw_sie()

    fig_list = [fig1, fig2, fig3, fig4]
    sum_area = 0
    sum_circuit = 0
    for f in fig_list:
        sum_area += f.area()
        sum_circuit += f.circuit()


if __name__ == "__main__":
    main()
