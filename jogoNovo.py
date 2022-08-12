import csv
from logging import exception
import time
import numpy as np
import os
import keyboard
from funcoesJogo import formaPar, printaDificuldade
from termcolor import colored
from rank import rankingFacil, rankingMedio, rankingDificil
clear = lambda: os.system('cls')

def criaTabuleiro(dim):
    with open(f"{dim}.csv", newline='') as file:
        result_list = list(csv.reader(file))
        cartas = np.array(result_list)
        cartas = cartas.ravel()
        np.random.shuffle(cartas)
        cartas = cartas.reshape(dim,dim)
        
    return cartas

def dificuldade():
    global dimensao
    dimensao = 0
    printaDificuldade()
    print("Pressione o modo que deseja")
    while True:
        if keyboard.is_pressed('4'): 
            dimensao = 4
            break
        if keyboard.is_pressed('5'): 
            dimensao = 6
            break
        if keyboard.is_pressed('6'): 
            dimensao = 8
            break      
    
    clear()
    global start
    start = time.time()
    return dimensao
    
        

def seleciona(tabuleiro):
    while True:
        clear()
        imprimeTabuleiro(tabuleiro)
        x1,y1 = recebeCoord(tabuleiro)
        clear()
        imprimeTabuleiro(tabuleiro,x1-1,y1-1)
        x2,y2 = recebeCoord(tabuleiro)
        clear()
        imprimeTabuleiro(tabuleiro,x1-1,y1-1,x2-1,y2-1)
        if x1 == x2 and y1 == y2:
            print("Valores duplicados")
            time.sleep(1)
        else: break
    if tabuleiro[y1-1][x1-1] == tabuleiro[y2-1][x2-1]: formaPar(tabuleiro,x1,y1,x2,y2)    
    else:
        print("não formou par")
        time.sleep(1)
    
    if (tabuleiro == "0").all():  
        clear()
        print("Parabens você venceu o jogo")
        end = time.time()
        from jogoNovo import start
        tempo1 = time.strftime("%H:%M:%S", time.gmtime(end - start))
        nome_player = input('digite o nome do player: ')
        adicionaPlayer(nome_player,tempo1)
        print(f'{nome_player}, Seu tempo foi: {tempo1}'  )
        time.sleep(1)
        from menuPrincipal import menu
        menu()
        return False

    else: return True    


def imprimeTabuleiro(tabuleiro,x1 = None,y1 = None,x2 = None,y2 = None):
    print(" ",end="")
    #numero coluna
    for i in range(len(tabuleiro[0])):
        print("     ",i+1,end="")
    print("\n")
    for i in range(len(tabuleiro)):
        print(i+1,"  ",end = "")
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == "0":
                print(" "*7, end="")
            else:
                if (y1 == i and x1 == j) or (y2 == i and x2 == j): print(colored(tabuleiro[i][j], "red"), end="")
                else:
                    print(tabuleiro[i][j], end="")           
        print("\n")   


def recebeCoord(tab):
    while True:
        try:    
            coordx,coordy = map(int, input("Informe um valor valido para coordenadas de X e Y (formato XY) "))
            if (coordx > dimensao or coordx < 1  or coordy > dimensao or coordy < 1):
                raise exception
        except:
            print("Coordenada inválida",end="\r")
            time.sleep(1)
            continue
        if (tab[coordy-1][coordx-1] == "0"):
            print("Carta não existe", end="\r")
            time.sleep(1)
        else: 
            break
    return coordx, coordy

def adicionaPlayer(player,tempo):
    if dimensao == 4:
        rankingFacil.append([player,tempo])
    elif dimensao == 6:
        rankingMedio.append([player,tempo])
    elif dimensao == 8:
        rankingDificil.append([player,tempo])
