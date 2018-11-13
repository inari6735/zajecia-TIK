#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  klasa01.py

class Osoba():
    """ Prosta klasa opisująca osobę """
    
    def __init__(self, imie, nazwisko, hp):
        self.imie = imie
        self.nazwisko = nazwisko
        self.ustawPlec(imie)
        self.hp = hp
        
    def ustawPlec(self, imie):
        if imie[-1] == "a": # ostatni znak imienia
            self.plec = "Kobieta"
            self.atak = 3
            self.blok = 1
        else:
            self.plec = "Mężczyzna"
            self.atak = 5
            self.blok = 2
            
    def atakuj(self, osoba):
        osoba.blokuj(self.atak)
    
    def blokuj(self, atak):
        self.hp = (atak - self.blok)
        if self.hp < 1:
            print("I'm dead")
        else:
            print("I'm still alive! Hit me one more time")
        
jakub = Osoba('Kuba', 'Gwizd', 10)
print(jakub.imie, jakub.nazwisko, jakub.plec)
michal = Osoba('Michał', 'Świst', 10)
print(michal.imie, michal.nazwisko, michal.plec)
jakub.atakuj(michal)
michal.atakuj(jakub)
print(jakub.hp, michal.hp)
