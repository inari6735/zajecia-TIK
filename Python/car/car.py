#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  car.py
#
# napisz definicję obiektu samochód z następującymi atrybutami:
# marka, np. "Fiat"
# model, np. "Tipo"
# rok produkcji, np. "2005"
# nadwozie, np. "sedan"
# metody obiektu:
# wiek() - zwraca wiek auta w latach

from datetime import date

class Car():
    
    def __init__(self, marka, model, rocznik, nadwozie):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.nadwozie = nadwozie

    def wiek(self, rocznik):
        self.dzis = date.today().year
        self.wiek = self.dzis - self.rocznik
        print(self.wiek)

car1 = Car('BMW', 'M3', 2004, 'sedan')
print(car1.marka, car1.model, car1.rocznik, car1.nadwozie)
car1.wiek(car1)
