# encoding:utf-8
import sys

def escreveMatriz(matriz, linha):
	for i in range(linha):
		print('\t'.join(int(i) for i in matriz[i]))

def smithWaterman(sequencia1, sequencia2, match, mismatch, gap,  status):
    tamanhoSequencia1 = len(sequencia1)
    tamanhoSequencia2 = len(sequencia2)
    linha = (tamanhoSequencia1 + 1)
    coluna = (tamanhoSequencia2 + 1)

    #Criando matriz e inicializando com 0
    matriz = [[0] * coluna for i in range(linha)]
    direcao = {}

    for i in range(1, coluna):
        direcao[(0, i)] = (0, i-1)

    for i in range(1, linha):
        direcao[(0, i)] = (i-1, 0)
    
    informacaoMaxValor = 3 * [-1]

    def maxValor(i, j):
        #print('ENTROU')
        print(sequencia1[i-1])
        print(sequencia2[j-1])
        if (sequencia2[i-1] == sequencia1[j-1]):
            print('==')
            score = match
        else:
            print('!=')            
            score = mismatch
        
        diagonal = int(matriz[i-1][j-1])+int(score)
        valor1 = diagonal
        valor2 = int(matriz[i-1][j]) + int(gap)
        valor3 = int(matriz[i][j-1]) + int(gap)
        maxValorTotal = max([0, valor1, valor2, valor3])
        #print('TOTAL: ',maxValorTotal)
        if maxValorTotal == valor1:
            direcao[(i, j)] = (i-1, j-1)
        elif maxValorTotal == valor2:
            direcao[(i, j)] = (i-1, j)
        else:
            direcao[(i, j)] = (i, j-1)

        if informacaoMaxValor[0] <= maxValorTotal:
            informacaoMaxValor[0] = maxValorTotal
            informacaoMaxValor[1] = i
            informacaoMaxValor[2] = j
        
        return maxValorTotal
    print('\n')
    print('LINHA: ', linha)
    print('COLUNA: ', coluna)
    print('\n')
    for i in range(1, linha):
        print('I: ', i)
        for j in range(1, coluna):
            print('J: ', j)
            #print('RETORNO: ', matriz[i][j])
            matriz[i][j] = maxValor(i, j)
            #print('MATRIZ: ', matriz[i][j])
        print('\n')
    

    print('Entrou')
    resultadoSequencia1 = ''
    resultadoSequencia2 = ''    
    
    i = informacaoMaxValor[1]
    j = informacaoMaxValor[2]

    while True:
        iProx, jProx = direcao[(i, j)]

        if (i-1) == iProx and (j-1) == jProx: #Diagonal
            resultadoSequencia1 += sequencia1[jProx]
            resultadoSequencia2 += sequencia2[iProx]
        elif (i-1) == iProx and j == jProx: # top
            resultadoSequencia1 += '-'
            resultadoSequencia2 += sequencia2[iProx]
        elif i == iProx and (j - 1) == jProx: # left
            resultadoSequencia1 += sequencia1[jProx]
            resultadoSequencia2 += '-'
        
        i = iProx
        j = jProx
        if not matriz[i][j] or (not i and not j):
            break

    resultadoSequencia1 = resultadoSequencia1[::-1]
    resultadoSequencia2 = resultadoSequencia2[::-1]
	
    if status:
        print('MATRIZ:\n')
        escreveMatriz(matriz, linha)
        print('\nSEQUÊNCIA 1: %s' % resultadoSequencia1)
        print('SEQUÊNCIA 2: %s\n' % resultadoSequencia2)
    return (resultadoSequencia1, resultadoSequencia2)    

if __name__ == "__main__":
    match = 2
    mismatch = -1
    gap = -1

    sequencia1 = raw_input('Forneça a primeira sequência: ')
    sequencia2 = raw_input('Forneça a segunda sequência: ')
    match = raw_input('Forneça o Match: ')
    mismatch = raw_input('Forneça o Mismatch: ')
    gap = raw_input('Forneça o GAP: ')
    smithWaterman(sequencia1, sequencia2, match, mismatch, gap, True)
    
    # tamanho_sys_argumento = len(sys.argv)
    #sequencia1 = sys.argv[1]
    #sequencia2 =  sys.argv[2]
    
    
    # if tamanho_sys_argumento > 3:
    #     match = int(sys.argv[3])
    #     if tamanho_sys_argumento > 4:
    #         mismatch = int(sys.argv[4])
    #         if tamanho_sys_argumento > 5:
    #             gap = int(sys.argv[5])
