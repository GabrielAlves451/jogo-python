import os


clear = lambda: os.system('cls')
rankingFacil = list()
rankingMedio = list()
rankingDificil = list()

def imprimeRanking(lista):
    listaOrdenada = sorted(lista, key=lambda tup: tup[1])
    clear()
    for i in range(len(listaOrdenada)):
        print(i+1, end = "")
        print(". Player: ",listaOrdenada[i][0],end="")
        print(". Tempo: ",listaOrdenada[i][1])
        

    

