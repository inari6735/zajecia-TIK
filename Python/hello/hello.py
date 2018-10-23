#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  hello.py

print("Wtyczki do SublimeText: Anaconda, Emmet, SublimeREPL, ColorPicker, GitSavvy")

def witaj():
    print("Hello World!")
    a = int(input("Podaj liczbę 1: "))
    b = int(input("Podaj liczbę 2: "))
    print(a + b)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(witaj())
