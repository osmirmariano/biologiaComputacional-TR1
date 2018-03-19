# encoding:utf-8
import sys

def show_pretty_matrix(matrix, rows):
	for i in range(rows):
		print('\t'.join(str(i) for i in matrix[i]))

def get_score(sequencia1, sequencia2, match, mismatch, gap):
	len_s, score = len(sequencia1), 0
	for i in range(len_s):
		if sequencia1[i] != '-' and sequencia2[i] != '-':
			if sequencia1[i] == sequencia2[i]:
				score += match
			else:
				score += mismatch
		else:
			score += gap
	return score

def needleman_wunsch(sequencia1, sequencia2, match, mismatch, gap, verbose=True):

	if verbose:
		print('\nSequence 1: %s' % sequencia1)
		print('Sequence 2: %s' % sequencia2)

	cols, rows = len(sequencia1) + 1, len(sequencia2) + 1
	
	# creates the matrix
	matrix = [[0 for x in range(cols)] for x in range(rows)]

	# directions for to reconstruct the path
	directions = {}

	# fills first column and first line
	matrix[0][0] = 0
	for i in range(1, cols):
		matrix[0][i] = matrix[0][i - 1] + gap
		directions[(0, i)] = (0, i - 1)
	for i in range(1, rows):
		matrix[i][0] = matrix[i - 1][0] + gap
		directions[(i, 0)] = (i - 1, 0)


	# function that returns the maximum value
	def max_value(i, j):

		value1 = matrix[i - 1][j - 1] + (match if sequencia2[i - 1] == sequencia1[j - 1] else mismatch) # left diagonal
		value2 = matrix[i - 1][j] + gap # top
		value3 = matrix[i][j - 1] + gap # left

		# calculates max value
		max_value = max([value1, value2, value3])

		# checks max value
		if max_value == value1:
			directions[(i,j)] = (i - 1, j - 1)
		elif max_value == value2:
			directions[(i,j)] = (i - 1, j)
		else:
			directions[(i,j)] = (i, j - 1)

		return max_value


	# fills remaining of the matrix
	for i in range(1, rows):
		for j in range(1, cols):
			matrix[i][j] = max_value(i, j)

	resultadoSequencia1, resultadoSequencia2 = '', '' # alignment results
	i, j = rows - 1, cols - 1 # starting with the last value

	while True:

		i_next, j_next = directions[(i, j)]

		if (i - 1) == i_next and (j - 1) == j_next: # diagonal
			resultadoSequencia1 += sequencia1[j_next]
			resultadoSequencia2 += sequencia2[i_next]
		elif (i - 1) == i_next and j == j_next: # top
			resultadoSequencia1 += '-'
			resultadoSequencia2 += sequencia2[i_next]
		elif i == i_next and (j - 1) == j_next: # left
			resultadoSequencia1 += sequencia1[j_next]
			resultadoSequencia2 += '-'

		i, j = i_next, j_next
		if not i and not j:
			break

	resultadoSequencia1, resultadoSequencia2 = resultadoSequencia1[::-1], resultadoSequencia2[::-1]

	if verbose:
		print('\nMatrix:\n')
		show_pretty_matrix(matrix, rows)
		print('\nSequence 1: %s' % resultadoSequencia1)
		print('Sequence 2: %s\n' % resultadoSequencia2)

	return (resultadoSequencia1, resultadoSequencia2)

if __name__ == "__main__":
	
	tamanho_sys_argumento = len(sys.argv)
	if tamanho_sys_argumento == 2 or tamanho_sys_argumento == 6:
		if tamanho_sys_argumento == 6:
			sequencia1, sequencia2 = sys.argv[1], sys.argv[2]
			match, mismatch, gap = sys.argv[3], sys.argv[4], sys.argv[5]
			needleman_wunsch(sequencia1, sequencia2, int(match), int(mismatch), int(gap))