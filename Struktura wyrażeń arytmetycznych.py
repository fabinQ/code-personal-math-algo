from abc import ABC, abstractmethod
import math
class Wezel(ABC):

    @abstractmethod
    def oblicz_wartosc(self):
        pass

    @abstractmethod
    def nazwa(self):
        pass

    def wypisz(self):
        print(f"Właśnie wykonuje {self.nazwa()}", end=' ')


class Liczba(Wezel):

    def __init__(self, liczba):
        self.liczba = liczba

    def oblicz_wartosc(self):
        return self.liczba

    def nazwa(self):
        return 'liczbą'

    def wypisz(self):
        print(f"Jestem liczbą {self.liczba}")


class Suma(Wezel):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def oblicz_wartosc(self):
        return self.a.oblicz_wartosc() + self.b.oblicz_wartosc()

    def nazwa(self):
        return 'dodawanie'

    def wypisz(self):
        self.a.wypisz()
        self.b.wypisz()
        super().wypisz()
        print(f"{self.a.oblicz_wartosc()}+{self.b.oblicz_wartosc()}={self.oblicz_wartosc()}")

class Roznica(Wezel):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def oblicz_wartosc(self):
        return self.a.oblicz_wartosc() - self.b.oblicz_wartosc()

    def nazwa(self):
        return 'odejmowanie'

    def wypisz(self):
        self.a.wypisz()
        self.b.wypisz()
        super().wypisz()
        print(f"{self.a.oblicz_wartosc()}-{self.b.oblicz_wartosc()}={self.oblicz_wartosc()}")

class Iloczyn(Wezel):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def oblicz_wartosc(self):
        return self.a.oblicz_wartosc() * self.b.oblicz_wartosc()

    def nazwa(self):
        return 'mnożenie'

    def wypisz(self):
        self.a.wypisz()
        self.b.wypisz()
        super().wypisz()
        print(f"{self.a.oblicz_wartosc()}*{self.b.oblicz_wartosc()}={self.oblicz_wartosc()}")
class Iloraz(Wezel):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def oblicz_wartosc(self):
        return self.a.oblicz_wartosc() / self.b.oblicz_wartosc()

    def nazwa(self):
        return 'dzielenie'

    def wypisz(self):
        self.a.wypisz()
        self.b.wypisz()
        super().wypisz()
        print(f"{self.a.oblicz_wartosc()}/{self.b.oblicz_wartosc()}={self.oblicz_wartosc()}")

class Silnia(Wezel):

    def __init__(self, a):
        self.a = a

    def oblicz_wartosc(self):
        return math.factorial(int(self.a.oblicz_wartosc()))

    def nazwa(self):
        return 'silnia'

    def wypisz(self):
        self.a.wypisz()
        super().wypisz()
        print(f"{self.a.oblicz_wartosc()}!={self.oblicz_wartosc()}")

def main():
    minus_jeden = Liczba(1)
    cztery = Liczba(4)
    piec = Liczba(5)
    siedem = Liczba(7)
    osiem = Liczba(8)

    dodawanie = Suma(piec, siedem)
    odejmowanie = Roznica(dodawanie, cztery)
    mnozenie = Iloczyn(odejmowanie, osiem)
    dzielenie = Iloraz(mnozenie, minus_jeden)
    silnia = Silnia(dzielenie)

    silnia.wypisz()


if __name__ == "__main__":
    main()
