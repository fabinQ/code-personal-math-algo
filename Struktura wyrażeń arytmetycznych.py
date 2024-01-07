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
        print(f"Właśnie wykonuje {self.nazwa()}")


class Liczba(Wezel):

    def __init__(self, liczba):
        self.liczba = liczba

    def oblicz_wartosc(self):
        return self.liczba

    def nazwa(self):
        return 'liczbą'

    def wypisz(self):
        print(f"Jestem liczbą {self.oblicz_wartosc()}")


class Suma(Wezel):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def oblicz_wartosc(self):
        return self.a.oblicz_wartosc() + self.b.oblicz_wartosc()

    def nazwa(self):
        return 'dodawanie'

    def wypisz(self):
        print(f"Właśnie dodaje {self.a.oblicz_wartosc()} i {self.b.oblicz_wartosc()} a ich suma to {self.oblicz_wartosc()}")


class Roznica(Wezel):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def oblicz_wartosc(self, a, b):
        return self.a.oblicz_wartosc() - self.b.oblicz_wartosc()

    def nazwa(self):
        return 'odejmowanie'

    def wypisz(self):
        print(f"Właśnie odejmuje {self.a.oblicz_wartosc()} i {self.b.oblicz_wartosc()} a ich różnica to {self.oblicz_wartosc()}")


class Iloczyn(Wezel):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def oblicz_wartosc(self):
        return self.a.oblicz_wartosc() * self.b.oblicz_wartosc()

    def nazwa(self):
        return 'mnożenie'

    def wypisz(self):
        print(f"Właśnie mnożę {self.a.oblicz_wartosc()} i {self.b.oblicz_wartosc()} a ich iloczyn to {self.oblicz_wartosc()}")

class Iloraz(Wezel):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def oblicz_wartosc(self, a, b):
        return self.a.oblicz_wartosc() / self.b.oblicz_wartosc()

    def nazwa(self):
        return 'dzielenie'

    def wypisz(self):
        print(f"Właśnie dzielę {self.a.oblicz_wartosc()} i {self.b.oblicz_wartosc()} a ich iloraz to {self.oblicz_wartosc()}")


class Silnia(Wezel):

    def __init__(self, a):
        self.a = a

    def oblicz_wartosc(self):
        return math.factorial(self.a.oblicz_wartosc())

    def nazwa(self):
        return 'silnia'

    def wypisz(self):
        self.a.wypisz()
        super().wypisz()
        print(f"Właśnie obliczam silnię {self.a.oblicz_wartosc()}, a wynik to {self.oblicz_wartosc()}")


def main():
    minus_jeden = Liczba(-1)
    cztery = Liczba(4)
    piec = Liczba(5)
    siedem = Liczba(7)
    osiem = Liczba(8)

    dodawanie = Suma(piec, siedem)
    odejmowanie = Roznica(osiem, cztery)
    mnozenie = Iloczyn(dodawanie, odejmowanie)
    dzielenie = Iloraz(mnozenie, minus_jeden)
    silnia = Silnia(dzielenie)

    silnia.wypisz()


if __name__ == "__main__":
    main()
