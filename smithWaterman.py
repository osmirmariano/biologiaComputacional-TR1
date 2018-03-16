#coding: utf-8
import sys

class AlinhamentoSmithWaterman():
    #Caracteres iguais
    match = 1
    #Caracteres diferentes
    mismatch = -1
    #Lacunas
    gap = -1
    
    sequencia1 = raw_input('Forneça a primeira sequência: ')
    sequencia2 = raw_input('Forneça a segunda sequência: ')
    
    matrix = []
    for i in range(len(sequencia1)):
        matrix.append([len(sequencia1)]*len(sequencia2))
        for j in range(len(sequencia2)):
            if(i == 0 or j == 0):
                matrix[i][j] = 0
            else:
                matrix[i][j] = 1
            print(matrix[i][j]) 
        print('\n') 