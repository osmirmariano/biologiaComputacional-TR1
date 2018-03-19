# encoding:utf-8
import sys

#Função para escrever a matriz gerada
def escreveMatriz(matriz, linha):
	for i in range(linha):
		print('\t '.join(str(i) for i in matriz[i]))

def get_score(sequencia1, sequencia2, match, mismatch, gap):
	tamanho = len(sequencia1)
	score = 0
	for i in range(tamanho):
		if sequencia1[i] != '-' and sequencia2[i] != '-':
			if sequencia1[i] == sequencia2[i]:
				score += match
			else:
				score += mismatch
		else:
			score += gap
	return score

def needlemanWunsch(sequencia1, sequencia2, match, mismatch, gap, verbose=True):

	if verbose:
		print('\n--------------------INFORMAÇÕES RELEVANTES--------------------------')
		print('  SEQUÊNCIA 1: %s' % sequencia1)
		print('  SEQUÊNCIA 2: %s' % sequencia2)
		print('  MATCH: %s' % match)
		print('  MISMATCH: %s' % mismatch)
		print('  GAP: %s' % gap)
		print('--------------------------------------------------------------------')	


	coluna, linha = len(sequencia1) + 1, len(sequencia2) + 1
	
	#Criando e inicializando a matriz
	matriz = [[0 for x in range(coluna)] for x in range(linha)]

	#Variável para a reconstrução do caminho
	direcao = {}

	#Preencher a primeira coluna e primeira linha da matriz
	matriz[0][0] = 0
	for i in range(1, coluna):
		matriz[0][i] = matriz[0][i - 1] + gap
		direcao[(0, i)] = (0, i - 1)
	for i in range(1, linha):
		matriz[i][0] = matriz[i - 1][0] + gap
		direcao[(i, 0)] = (i - 1, 0)

	#Função que vai retornar o máximo valor
	def max_value(i, j):
		if sequencia2[i-1] == sequencia1[j-1]:
			score = match
		else:
			score = mismatch
		

		diagonal = matriz[i-1][j-1] + score
		topo = matriz[i-1][j] + score
		esquerdo = matriz[i][j-1] + gap
		#Obtem o máximo valor das variáveis diagonal, topo e esquerdo com a função max
		max_value = max([diagonal, topo, esquerdo])

		#Checa o máximo valor
		if max_value == diagonal:
			direcao[(i,j)] = (i - 1, j - 1)
		elif max_value == topo:
			direcao[(i,j)] = (i - 1, j)
		else:
			direcao[(i,j)] = (i, j - 1)

		return max_value


	#Preenche o restante da matriz
	for i in range(1, linha):
		for j in range(1, coluna):
			matriz[i][j] = max_value(i, j)

	resultadoSequencia1 = ''
	resultadoSequencia2 = ''
	#Inicializando i e j com o último valor
	i = linha - 1
	j = coluna - 1 

	while True:

		iProx, jProx = direcao[(i, j)]

		if (i - 1) == iProx and (j - 1) == jProx: #Para diagonal
			resultadoSequencia1 += sequencia1[jProx]
			resultadoSequencia2 += sequencia2[iProx]
		elif (i - 1) == iProx and j == jProx: #Para topo
			resultadoSequencia1 += '-'
			resultadoSequencia2 += sequencia2[iProx]
		elif i == iProx and (j - 1) == jProx: #Para esquerdo
			resultadoSequencia1 += sequencia1[jProx]
			resultadoSequencia2 += '-'

		i = iProx
		j = jProx
		if not i and not j:
			break

	resultadoSequencia1, resultadoSequencia2 = resultadoSequencia1[::-1], resultadoSequencia2[::-1]

	if verbose:
		print('\n-------------------------------MATRIZ-------------------------------')
		escreveMatriz(matriz, linha)
		print('--------------------------------------------------------------------')			
		print('\nRESULTADO SEQUÊNCIA 1: %s' % resultadoSequencia1)
		print('RESULTADO SEQUÊNCIA 2: %s\n' % resultadoSequencia2)

	return (resultadoSequencia1, resultadoSequencia2)

if __name__ == "__main__":
	
	tamanho_sys_argumento = len(sys.argv)
	if tamanho_sys_argumento == 2 or tamanho_sys_argumento == 6:
		if tamanho_sys_argumento == 6:
			sequencia1 = sys.argv[1]
			sequencia2 = sys.argv[2]
			match = sys.argv[3]
			mismatch = sys.argv[4]
			gap = sys.argv[5]
			needlemanWunsch(sequencia1, sequencia2, int(match), int(mismatch), int(gap))