import os
import time


clear = lambda: os.system('cls')

def formaPar(tab,x1,y1,x2,y2):
    print("Parabens formou par")
    time.sleep(0.8)
    tab[y1-1][x1-1],tab[y2-1][x2-1] = "0","0"

def printaDificuldade():
    clear()
    print(" ________________")
    print('|4 -  Modo Facil |')
    print(" \u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305")
    print(" ________________")
    print('|5 -  Modo Medio |')
    print(" \u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305")
    print(" ________________")
    print('|6 - Modo Dificil|')
    print(" \u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305")    