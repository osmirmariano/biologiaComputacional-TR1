#coding: utf-8
import sys

class AlinhamentoSmithWaterman():
    #Caracteres iguais
    match = 1
    #Caracteres diferentes
    mismatch = -1
    #Lacunas
    gap = -4
    
    sequencia1 = raw_input('Forneça a primeira sequência: ')
    sequencia2 = raw_input('Forneça a segunda sequência: ')
        
    novaSequencia1 = '-'
    novaSequencia2 = '-'

    for i in range(len(sequencia1)):
        novaSequencia1 += sequencia1[i]
    print(novaSequencia1)

    for j in range(len(sequencia2)):
        novaSequencia2 += sequencia2[j]
    print(novaSequencia2)

    tamanhoSequencia1 = len(novaSequencia1)
    tamanhoSequencia2 = len(novaSequencia2)
    matrix = []

    for i in range(tamanhoSequencia1):
        matrix.append([tamanhoSequencia1]*tamanhoSequencia2)
        for j in range(tamanhoSequencia2):
            if(i == 0 or j == 0):
                matrix[i][j] = 0
            else:
                if(novaSequencia1[i] == novaSequencia2[j]):
                    print(novaSequencia1[i])
                    print(novaSequencia2[j])
                    
                #if(matrix[])
                #diagonal = matrix[i-1][j-1]
                matrix[i][j] = 1
            print(matrix[i][j]) 
        print('\n') 