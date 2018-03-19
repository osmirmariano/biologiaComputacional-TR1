# encoding:utf-8
import sys

def escreveMatriz(matriz, linha):
	for i in range(linha):
		print('\t'.join(str(i) for i in matriz[i]))


def smithWaterman(sequencia1, sequencia2, match=2, mismatch=-1, gap=-1, status=True):
	tamanhoSequencia1 = len(sequencia1)
	tamanhoSequencia2 = len(sequencia2)
	#Tamanho da matriz
	linha = (tamanhoSequencia2 + 1)
	coluna = (tamanhoSequencia1 + 1)

	#Criando e incializando a matriz
	matriz = [[0] * coluna for i in range(linha)]

	#Variável para a reconstrução do caminho
	direcao = {}

	for i in range(1, coluna):
		direcao[(0, i)] = (0, i - 1)
	for i in range(1, linha):
		direcao[(i, 0)] = (i - 1, 0)

	#informacaoMaxValor é uma lista com 3 elementos: max_value, posição da linha, posição coluna
	informacaoMaxValor = 3 * [-1]

	#Função para retornar o valor Máximo
	def max_value(i, j):
		if (sequencia2[i-1] == sequencia1[j-1]):
			score = match
		else:
			score = mismatch

		diagonal = matriz[i-1][j-1] + score #Diagonal
		topo = matriz[i-1][j] + gap #Topo
		esquerda = matriz[i][j-1] + gap #Esquerda

		#Calcular o máximo valor
		max_value = max([0, diagonal, topo, esquerda])

		#Checando máximo valor
		if max_value == diagonal:
			direcao[(i,j)] = (i-1, j-1)
		elif max_value == topo:
			direcao[(i,j)] = (i-1, j)
		else:
			direcao[(i,j)] = (i, j-1)

		#Verifica pontuação mais alta
		if informacaoMaxValor[0] <= max_value:
			informacaoMaxValor[0], informacaoMaxValor[1], informacaoMaxValor[2] = max_value, i, j

		return max_value


	#Para preencher a matriz de acordo com o algoritmo
	for i in range(1, linha):
		for j in range(1, coluna):
			matriz[i][j] = max_value(i, j)

	#Variável para alinhamento dos resultados
	resultadoSequencia1 = ''
	resultadoSequencia2 = '' 

	#Alinhamento começa na maior célula de pontuação na matriz
	i = informacaoMaxValor[1]
	j = informacaoMaxValor[2]

	while True:
		iProx, jProx = direcao[(i, j)]
		if (i - 1) == iProx and (j - 1) == jProx: #Diagonal
			resultadoSequencia1 += sequencia1[jProx]
			resultadoSequencia2 += sequencia2[iProx]
		elif (i - 1) == iProx and j == jProx: #Topo
			resultadoSequencia1 += '-'
			resultadoSequencia2 += sequencia2[iProx]
		elif i == iProx and (j - 1) == jProx: #Esquerda
			resultadoSequencia1 += sequencia1[jProx]
			resultadoSequencia2 += '-'

		i, j = iProx, jProx
		if not matriz[i][j] or (not i and not j):
			break

	resultadoSequencia1 = resultadoSequencia1[::-1]
	resultadoSequencia2 = resultadoSequencia2[::-1]

	if status:
		print('\n--------------------INFORMAÇÕES RELEVANTES--------------------------')
		print('  SEQUÊNCIA 1: %s' % sequencia1)
		print('  SEQUÊNCIA 2: %s' % sequencia2)
		print('  MATCH: %s' % match)
		print('  MISMATCH: %s' % mismatch)
		print('  GAP: %s' % gap)
		print('--------------------------------------------------------------------')	

		print('\n-------------------------------MATRIZ-------------------------------')
		escreveMatriz(matriz, linha)
		print('--------------------------------------------------------------------')			
		print('\nSEQUÊNCIA 1: %s' % resultadoSequencia1)
		print('SEQUÊNCIA 2: %s\n' % resultadoSequencia2)

	return (resultadoSequencia1, resultadoSequencia2)



if __name__ == "__main__":
	tamanho_sys_argumento = len(sys.argv)
	sequencia1 = sys.argv[1]
	sequencia2 = sys.argv[2]

	match, mismatch, gap = 2, -1, -1

	if tamanho_sys_argumento > 3:
		match = int(sys.argv[3])
		if tamanho_sys_argumento > 4:
			mismatch = int(sys.argv[4])
			if tamanho_sys_argumento > 5:
				gap = int(sys.argv[5])

	# runs the algorithm
	smithWaterman(sequencia1, sequencia2, match=match, mismatch=mismatch, gap=gap)