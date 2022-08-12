import sys
import time

from colorama import Fore
from jogoNovo import dificuldade, criaTabuleiro, imprimeTabuleiro, seleciona
import os
import keyboard
from rank import imprimeRanking,rankingFacil, rankingMedio, rankingDificil
clear = lambda: os.system('cls')

def menu():
    clear()
    print(" ____    ____       _       ____  ____     _____   ___   ____  _____   ______")
    print("|_   \  /   _|     / \     |_   ||   _|   |_   _|.'   `.|_   \|_   _|.' ___  |") 
    print("  |   \/   |      / _ \      | |__| |       | | /  .-.  \ |   \ | | / .'   \_|")
    print("  | |\  /| |     / ___ \     |  __  |   _   | | | |   | | | |\ \| | | |   ____") 
    print("_ | |_\/_| |_  _/ /   \ \_  _| |  | |_ | |__' | \  `-'  /_| |_\   |_\ `.___]  |")
    print("|_____||_____||____| |____||____||____|`.____.'  `.___.'|_____|\____|`._____.'") 
    print("\n")
    printaMenu()
    # Validador de numero e string
    print("Pressiona a opção que deseja")
    while True: 
        if keyboard.is_pressed('1'):
            jogar()
            break 
        if keyboard.is_pressed('2'): 
            ranking()
            break
        if keyboard.is_pressed('3'): 
            clear()
            creditos()
        if keyboard.is_pressed('4'): 
            clear()
            print("Jogo encerrado")
            time.sleep(1)
            sair()
            

    
       
def jogar():
    cartas = criaTabuleiro(dificuldade())
    imprimeTabuleiro(cartas)
    seleciona(cartas)
   
    while  seleciona(cartas):
        pass
    

def ranking():
    clear()
    print("4 - Ranking Facil\n5 - Ranking Medio\n6 - Ranking Dificil")
    
    while True: 
        if keyboard.is_pressed('4'):
            clear()
            imprimeRanking(rankingFacil)
            break 
        if keyboard.is_pressed('5'): 
            clear()
            imprimeRanking(rankingMedio)
            break
        if keyboard.is_pressed('6'): 
            clear()
            imprimeRanking(rankingDificil)
            break
    print("Para retorna para o menu, pressione ESC")
    while True: 
            try:  
                if keyboard.is_pressed('esc'):  
                    menu()
                    break 
            except:        
                ...
def sair():
    sys.exit()

def creditos():
    print("Progamadores: ")
    print("André Luís Bastos de Azevedo Silveira\nBreno Henrique da Silva Peixoto\nGabriel Alves Oliveira Ribeiro\nPaulo Francisco da Silva")
    print("Para retorna para o menu, pressione ESC")
    while True: 
            try:  
                if keyboard.is_pressed('esc'):  
                    menu()
                    break 
            except:        
                ...
def printaMenu():
    print(" ___________")
    print('|1 -  Jogar |')
    print(" \u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305")
    print(" ___________")
    print('|2 - Ranking|')
    print(" \u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305")
    print(" ___________")
    print('|3- Creditos|')
    print(" \u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305")
    print(" ___________")
    print('|4-  Sair  |')
    print(" \u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305","\u0305")
menu()    