import sys

def test(did_pass):
	"""  Print the result of a test.  """
	linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
	if did_pass:
		msg = "Test at line {0} ok.".format(linenum)
	else:
		msg = ("Test at line {0} FAILED.".format(linenum))
	print(msg)

def test_suite():
	""" 
	Run the suite of tests for code in this module (this file).
	"""
	test(abs(colMean([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 2) - 4.0) < .0000001 )
	test(colMode([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 2) == 3)
	# colStandardize (to be added)
	# colMinMaxNormalize(m, col): (to be added)
	#Proper normalize test for a short vector:
	test(abs(normalizeVector([6, 8])[0] - .6) < .0000001 )
	test(abs(normalizeVector([6, 8])[1] - .8) < .0000001 )
	#However, to test normalize you may paste in these correct vector elements, but to
	#whatever precision your system has
	test(normalizeVector([25, 2, 7, 1 ,-5 ,12]) == [0.8585035246793065,
	0.06868028197434452, 0.2403809869102058, 0.03434014098717226,
	-0.1717007049358613, 0.4120816918460671])
	test(abs(euclideanDistance([3, 1], [6, 5]) - 5) < .0000001)
	test(abs(euclideanDistance([0, 0], [3, 4]) - 5) < .0000001)
	test(euclideanDistance([3, 6, 1, 2, 8, 2, 1], [3, 6, 1, 2, 8, 2, 1]) == 0)

	test(colMean([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 2) == 4.0)
	test(colMean([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 4) == None)
	test(colMean([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 0) == 1.3333333333333333)
	test(colMean([[5, 6, 9, 12394], [6, 3, 1, -7]], 0) == 5.5)
	test(colMean([[5, 6, 9, 12394], [6, 3, 1, -7]], 1) == 4.5)
	test(colMean([[5, 6, 9, 12394], [6, 3, 1, -7]], 2) == 5.0)
	test(colMean([[5, 6, 9, 12394], [6, 3, 1, -7]], 3) == 6193.5)
	test(colMean([[5, 6, 9, 12394], [6, 3, 1, -7]], -4) == None)
	test(colMean([[5, 6, 9, 12394], [6, 3, 1, -7]], 4) == None)
	test(colMean([[1, 3, 5, 7, 9, 11, 13], [2, 4, 6, 8, 10, 12, 14]], 0 == 7))
	test(colMean([[1, 3, 5, 7, 9, 11, 13], [2, 4, 6, 8, 10, 12, 14]], 1 == 8))
	test(colMean([[1, 3, 5, 7, 9, 11, 13], [2, 4, 6, 8, 10, 12, 14]], 2 == None))
	test(colMean([[-1, -5.8, 69, 4,	0.2], [888, -6, -479.2, 0, 1111]], 1) == -5.9)
	test(colMean([[-1, -5.8, 69, 4,	0.2], [888, -6, -479.2, 0, 1111]], 3) == 2)
	test(colMean([[1, 4, 2], [1, 61, 6, 8]], 2) == None)

	test(colMode([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 2) == 3)
	test(colMode([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 0) == 1)
	test(colMode([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 1) == 2)
	test(colMode([[5, 6, 9, 12394], [6, 3, 1, -7]], 0) == "No mode")
	test(colMode([[5, 6, 9, 12394], [6, 3, 1, -7]], 1) == "No mode")
	test(colMode([[4, 3, 2, 1], [5,	4, 3, 2], [4, 3, 2,	1], [4, 4, 4, 4]], 0) == 4)
	test(colMode([[4, 3, 2, 1], [5,	4, 3, 2], [4, 3, 2,	1], [4, 4, 4, 4]], -1) == None)
	test(colMode([[4, 3, 2, 1], [5,	4, 3, 2], [4, 3, 2,	1], [4, 4, 4, 4]], 4) == None)
	test(colMode([[1, 2], [1, 2], [1, 3], [1, 4]], 0) == 1)
	test(colMode([[1, 2], [1, 2], [1, 3], [1, 4]], 1) == 2)
	test(colMode([[1, 2], [1, 2], [1, 3], [1, 4]], 2) == None)
	test(colMode([[1, 4, 2], [1, 61, 6, 8], [2, 2, 2, 2, 2]], 0) == None)

	test(colStandardize([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 2) == 
		[[2, 4, 1.1547005383792517], [1, 2, -0.5773502691896258], [1, 2, -0.5773502691896258]])
	test(colStandardize([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 0) == 
		[[1.1547005383792517, 4, 6], [-0.5773502691896256, 2, 3], [-0.5773502691896256, 2, 3]])
	test(colStandardize([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 1) == 
		[[2, 1.1547005383792517, 6], [1, -0.5773502691896256, 3], [1, -0.5773502691896256, 3]])
	test(colStandardize([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 3) == None)
	test(colStandardize([[4, 3, 2, 1], [5, -4, 3, 2]], 0) == 
		[[-0.7071067811865475, 3, 2, 1], [0.7071067811865475, -4, 3, 2]])
	test(colStandardize([[4, 3, 2, 1], [5, -4, 3, 2]], 1) == 
		[[4, 0.7071067811865476, 2, 1], [5, -0.7071067811865476, 3, 2]])
	test(colStandardize([[4, 3, 2, 1], [5, -4, 3, 2]], 2) == 
		[[4, 3, -0.7071067811865475, 1], [5, -4, 0.7071067811865475, 2]])
	test(colStandardize([[4, 3, 2, 1], [5, -4, 3, 2]], 3) == 
		[[4, 3, 2, -0.7071067811865475], [5, -4, 3, 0.7071067811865475]])
	test(colStandardize([[4, 3, 2, 1], [5, -4, 3, 2]], 4) == None)
	test(colStandardize([[0, -5], [0, 8], [0, 12], [0, 6]], 0) == 
		[[0, -5], [0, 8], [0, 12], [0, 6]])
	test(colStandardize([[0, -5], [0, 8], [0, 12], [0, 6]], 1) == 
		[[0, -1.409053963078115], [0, 0.3780388681429089], [0, 0.9279135854416855], [0, 0.10310150949352061]])
	test(colStandardize([[1, 1, 1, 1], [1, 0, -0.5, 8], [1, 0, 12, 3.15]], 0) == 
		[[0, 1, 1, 1], [0, 0, -0.5, 8], [0, 0, 12, 3.15]])
	test(colStandardize([[1, 1, 1, 1], [1, 0, -0.5, 8], [1, 0, 12, 3.15]], 1) == 
		[[1, 1.1547005383792515, 1, 1], [1, -0.5773502691896256, -0.5, 8], [1, -0.5773502691896256, 12, 3.15]])
	test(colStandardize([[1, 1, 1, 1], [1, 0, -0.5, 8], [1, 0, 12, 3.15]], 2) == 
		[[1, 1, -0.4639669759802292, 1], [1, 0, -0.6837408067077061, 8], [1, 0, 1.1477077826879352, 3.15]])
	test(colStandardize([[1, 1, 1, 1], [1, 0, -0.5, 8], [1, 0, 12, 3.15]], 3) == 
		[[1, 1, 1, -0.8505925466063129], [1, 0, -0.5, 1.1015870685557168], [1, 0, 12, -0.2509945219494038]])
	test(colStandardize([[1, 1, 1, 1], [1, 0, -0.5, 8], [1, 0, 12, 3.15]], 4) == None)
	test(colStandardize([[1, 4, 2, 8], [1, 61, 6, 8], [4, 4, 4, 7, 8]], 2) == None)

	test(colMinMaxNormalize([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 2) == 
		[[2, 4, 1.0], [1, 2, 0], [1, 2, 0]])
	test(colMinMaxNormalize([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 0) == 
		[[1.0, 4, 6], [0, 2, 3], [0, 2, 3]])
	test(colMinMaxNormalize([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 1) == 
		[[2, 1.0, 6], [1, 0, 3], [1, 0, 3]])	
	test(colMinMaxNormalize([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 3) == None)
	test(colMinMaxNormalize([[5, 15], [5, 5], [5, 4]], 0) == 
		[[0, 15], [0, 5], [0, 4]])
	test(colMinMaxNormalize([[5, 15], [5, 5], [5, 4]], 1) == 
		[[5, 1.0], [5, 0.09090909090909091], [5, 0]])
	test(colMinMaxNormalize([[5, 15], [5, 5], [5, 4]], 2) == None)
	test(colMinMaxNormalize([[5, 10, 15], [10, 15, 20], [-10, 1, -2]], 0) == 
		[[0.75, 10, 15], [1.0, 15, 20], [0, 1, -2]])
	test(colMinMaxNormalize([[5, 10, 15], [10, 15, 20], [-10, 1, -2]], 1) == 
		[[5, 0.6428571428571429, 15], [10, 1.0, 20], [-10, 0, -2]])
	test(colMinMaxNormalize([[5, 10, 15], [10, 15, 20], [-10, 1, -2]], 2) == 
		[[5, 10, 0.7727272727272727], [10, 15, 1.0], [-10, 1, 0]])
	test(colMinMaxNormalize([[1, 4, 2], [0, 0]], 1) == None)

	test(mutation("ACTCGG", 0, "G") == "GCTCGG")
	test(mutation("ACTCGG", 5, "C") == "ACTCGC")
	test(mutation("ACTCGG", 6, "C") == None)
	test(mutation("GCGCGCGGGGGGGGGAAAAATTTTTTTTCAGCAGCAGCAGCAGCCCCCC", 20, "G") == 
		"GCGCGCGGGGGGGGGAAAAAGTTTTTTTCAGCAGCAGCAGCAGCCCCCC")
	test(mutation("GCGCGCGGGGGGGGGAAAAATTTTTTTTCAGCAGCAGCAGCAGCCCCCC", 2, "T") == 
		"GCTCGCGGGGGGGGGAAAAATTTTTTTTCAGCAGCAGCAGCAGCCCCCC")
	test(mutation("GCGCGCGGGGGGGGGAAAAATTTTTTTTCAGCAGCAGCAGCAGCCCCCC", -3, "G") == 
		None)
	test(mutation("ACG", 2, "G") == "ACG")
	test(mutation("AAAA", 4, "U") == None)

	test(insertion("ACTCGG", 2, "AGC") == "ACAGCTCGG")
	test(insertion("ACTCGG", 6, "AGC") == "ACTCGGAGC")
	test(insertion("ACTCGG", 7, "AGC") == None)
	test(insertion("ACTCGG", 0, "AGCCCGA") == "AGCCCGAACTCGG")
	test(insertion("CAGCAGGGCACACC", 6, "CAGCAGCAGCAGCAG") == 
		"CAGCAGCAGCAGCAGCAGCAGGGCACACC")
	test(insertion("", 0, "TTTTTTTTTTTTTTTTTTT") == "TTTTTTTTTTTTTTTTTTT")
	test(insertion("CACTGCGACACCACTGGGGTCCCCCCTAGGGGAAAAAAAAAAAAAAAAAAAAAAAAA", 
		56, "AAAAAAAAAAAAAAAAA") == 
	"CACTGCGACACCACTGGGGTCCCCCCTAGGGGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

	test(deletion("ACTCGG", 5, 2) == "ACTCG")
	test(deletion("ACTCGG", 1, 2) == "ACGG")
	test(deletion("ACTCGG", 0, 5) == "G")
	test(deletion("ACTCGG", 6, 1) == None)
	test(deletion("CAGCAGCAGCAGCAGCAGCAGACCACACAAAAAA", 0, 10) == "AGCAGCAGCAGACCACACAAAAAA")
	test(deletion("CAGCAGCAGCAGCAGCAGCAGACCACACAAAAAA", 11, 22) == "CAGCAGCAGCAA")
	test(deletion("CAGCAGCAGCAGCAGCAGCAGACCACACAAAAAA", 2, 34) == "CA")
	test(deletion("TCAGGACGAGACTACATGC", 18, 58) == "TCAGGACGAGACTACATG")
	test(deletion("TCAGGACGAGACTACATGC", 0, 40) == "")
	test(deletion("CACTGCGACACCACTGGGGTCCCCCCTAGGGGAAAAAAAAAAAAAAAAAAAAAAAAA", 32, 29) ==
	"CACTGCGACACCACTGGGGTCCCCCCTAGGGG")
	test(deletion("CACTGCGACACCACTGGGGTCCCCCCTAGGGGAAAAAAAAAAAAAAAAAAAAAAAAA", 60, 29) ==
	None)
	test(deletion("CACTGCGACACCACTGGGGTCCCCCCTAGGGGAAAAAAAAAAAAAAAAAAAAAAAAA", 0, 57) ==
	"")

	test(euclideanDistance([3, 1], [6, 5]) == 5)
	test(euclideanDistance([0, 0], [3, 4]) == 5)
	test(euclideanDistance([-5, 2], [3, 4]) == 8.246211251235321)
	test(euclideanDistance([24, 8], [-25, 20]) == 50.44799302251776)
	test(euclideanDistance([-1, -2], [-1, -9]) == 7)
	test(euclideanDistance([23.64, -5.42], [2, 12]) == 27.78031677285196)
	test(euclideanDistance([3, 7], [3, 7]) == 0)
	test(euclideanDistance([5, 5], [5, 15]) == 10)
	test(euclideanDistance([0, 4.5], [-7, -4.5]) == 11.40175425099138)

	test(normalizeVector([6, 8]) == [0.6, 0.8])
	test(normalizeVector([12, 5]) == [0.9230769230769231, 0.38461538461538464])
	test(normalizeVector([7, 2]) == [0.9615239476408232, 0.27472112789737807])
	test(normalizeVector([2, 2]) == [0.7071067811865475, 0.7071067811865475])
	test(normalizeVector([-7, -6]) == [-0.7592566023652966, -0.6507913734559685])

def colMean(m, col):
	"""
	If col is valid return the mean of values in column col, else print "col out of bounds"
	and return.
	:param m: a matrix of numbers represented as a list of lists
	:param col: an integer that represents a valid column index of m
	:return: the float value that is the mode of the values in column col of m
	Example:
	>>> colMean([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 2)
	4.0
	"""
	col_sum = 0 
	col_mean = 0
#	print(len(m))
	for i in range(len(m)):
		if len(m[i]) != len(m[0]):
			print("Error! Invalid Matrix!")
			return None

	if col >= len(m[0]) or col < 0 :
		print("Error! Col out of bounds")
		return None

	for i in range(len(m)):
		col_sum += m[i][col]

#	print(col_sum)
	col_mean = col_sum /len(m) 
#	print(col_mean)
	return col_mean


def countX(lst, x):
	"""
	This is a helper function that counts how many element x is in the list.
	The function returns the count for the element.
	"""
	counter = 0

	for elem in lst:
		if elem == x:
			counter += 1

	return counter

def colMode(m, col):
	"""
	If col is valid return the mode of values in col else print "col out of bounds" and return.
	:param m: a matrix of integers represented as a list of lists
	:param col: an integer that represents a valid column index of m
	:return: the integer value that is the mean of the values in column col of m
	Example:
	>>> colMode([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 2)
	3
	"""
	appear_num = []
	counter = 0
	mode = 0

	for i in range(len(m)):
		if len(m[i]) != len(m[0]):
			print("Error! Invalid Matrix!")
			return None

	if col >= len(m[0]) or col < 0 :
		print("Error! Col out of bounds")
		return None

	for i in range(len(m)):
		appear_num.append(m[i][col])

	for i in range(len(appear_num)):
		count = countX(appear_num, appear_num[i])

		if count > counter:
			counter = count 
			mode = appear_num[i]

	if counter == 1:
		return "No mode"

	return mode 
	
def colStandardize(m, col):
	"""
	If col is valid return a new matrix identical to m except that the values in col are
	standardized, else print "col out of bounds" and return.
	:param m: a matrix of numbers represented as a list of lists
	:param col: an integer that represents a valid column index of m
	:return: a new matrix of the contents of m, with values in column col standardized
	Example:
	>>> colStandardize([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 2)
	[[2, 4, 1.155], [1, 2, -0.577], [1, 2, -0.577]]
	"""
	for i in range(len(m)):
		if len(m[i]) != len(m[0]):
			print("Error! Invalid Matrix!")
			return None

	if col >= len(m[0]) or col < 0:
		print("Error! Col out of bounds")
		return None

	#mean
	col_mean = colMean(m, col)

	#standard deviation
	n = len(m)
	sigma = 0
	temp_sum = 0

	for i in range(n):
		temp_sum += (m[i][col] - col_mean)**2 
	
	sigma = (temp_sum/(n-1))**0.5

	#standardization 
	standardized_col = []

	for i in range(n):
		if sigma == 0:
			standardized_col.append(0)
		else:
			value = (m[i][col]- col_mean)/sigma
			standardized_col.append(value)

	standardized_m = m 
	for i in range(len(standardized_m)):
		standardized_m[i][col] = standardized_col[i]

#	print(standardized_m)
	return standardized_m

def findMin(m, col):
	"""
	This helper function finds the minimum number in a given matrix at a specific 
	column.
	"""
	min_num = m[0][col]

	for i in range(len(m)):
		if m[i][col] < min_num:
			min_num = m[i][col] 

	return min_num

def findMax(m, col):
	"""
	This helper function finds the maximum number in a given matrix at a specific 
	column.
	"""
	max_num = m[0][col]

	for i in range(len(m)):
		if m[i][col] > max_num:
			max_num = m[i][col] 
			
	return max_num

def colMinMaxNormalize(m, col):
	"""
	If col is valid return a new matrix identical to m except that the values in col are
	Normalized, else print "col out of bounds" and return.
	:param m: a matrix of numbers represented as a list of lists
	:param col: an integer that represents a valid column index of m
	:return: a new matrix of the contents of m with values in column col normalized between 0 and 1
	Example:
	>>> colMinMaxNormalize([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 2)
	[[2, 4, 1], [1, 2, 0], [1, 2, 0]]
	"""
	for i in range(len(m)):
		if len(m[i]) != len(m[0]):
			print("Error! Invalid Matrix!")
			return None

	if col >= len(m[0]) or col < 0:
		print("Error! Col out of bounds")
		return None

	min_num = findMin(m, col)
	max_num = findMax(m, col) 
	max_min = 0
	norm_col = []

	max_min = max_num - min_num 

	for i in range(len(m)):
		if m[i][col] - min_num == 0 or max_min == 0:
			norm_col.append(0)
		else:
			norm_num = (m[i][col] - min_num)/max_min
			norm_col.append(norm_num)

	norm_m = m

	for i in range(len(norm_m)):
		norm_m[i][col] = norm_col[i]

#	print(norm_m)
	return norm_m

def mutation(dna, index, newNT):
	"""
	If index is valid return a string with that represents a SNP (single nucleotide
	polymorphism) of dna, else print "index out of bounds" and return None.
	:param dna: a string
	:param index: an integer such that 0 <= index < len(dna)
	:param newNT: a string to replace the character at index
	:return: a string composed of the characters of dna with the value at index replaced with newNT
	Example:
	>>> mutation("ACTCGG", 0, "G")
	"GCTCGG"
	"""
	if index >= len(dna) or index < 0:
		print("Error! index out of bounds")
		return None 

	dna_list = []
	for i in range(len(dna)):
		dna_list.append(dna[i])

#	print(dna_list)
	newdna = ""

	dna_list[index] = newNT

	for nt in dna_list:
		newdna += nt

#	print(dna_list)
#	print(newdna)
	return newdna

def insertion (dna, index, newNTs):
	"""
	If index is valid return a string that represents an insertion mutation of dna,
	else print "index out of bounds" and return.
	:param dna: a string
	:param index: an integer such that 0 <= index <= len(dna)
	:param newNTs: a string to insert into dna at position index
	:return: a string composed of the characters of dna with the value at index replaced with newNT
	Examples:
	>>> insertion ("ACTCGG", 6, "AGC")
	"ACTCGGAGC"
	>>> insertion ("ACTCGG", 7, "AGC")
	"Index out of bounds"
	"""
	if index < 0 or index > len(dna):
		print("Error! index out of bounds")
		return None

	dna_list =[]
	for i in range(len(dna)):
		dna_list.append(dna[i])

	temp_list1 = []
	temp_list2 = []
	new_dna = []
	newdna = ""
	
	if index == len(dna):
		dna_list.append(newNTs)
		new_dna = dna_list
	
	elif index < len(dna):
		for i in range(index):
			temp_list1.append(dna[i])
#		print(temp_list1)
		for j in range(index, len(dna)):
			temp_list2.append(dna[j])
#		print(temp_list2)
		temp_list1.append(newNTs)
		new_dna = temp_list1 + temp_list2
#		print(new_dna)
	
	for nt in new_dna:
		newdna += nt
#	print(newdna)
	return newdna

def deletion(dna, index, numNTdeleted ):
	"""
	If index is valid return a string that represents a deletion mutation of dna,
	else print "index out of bounds" and return.
	:param dna: a string
	:param index: an integer such that 0 <= index < len(dna)
	:param numNTdeleted: integer indicating how many characters to delete
	:return: a string composed of the characters of dna with up to numNTdeleted beginning at position index.
	Examples:
	>>> deletion("ACTCGG", 5, 2)
	"ACTCG"
	>>> deletion("ACTCGG", 1, 2)
	"ACGG”
	"""
	if index < 0 or index > len(dna)-1:
		print("Error! index out of bounds")
		return None
	
	dna_list = []
	newdna = ""

	if index+numNTdeleted > len(dna)-1:
		for i in range(index):
			dna_list.append(dna[i])
	elif index + numNTdeleted <= len(dna)-1:
		temp_list1 = []
		temp_list2 = []
		for i in range(index):
			temp_list1.append(dna[i])
		for j in range(index+numNTdeleted, len(dna)):
			temp_list2.append(dna[j])
		dna_list = temp_list1 + temp_list2

	for nt in dna_list:
		newdna += nt 

#	print(newdna)
	return newdna

def euclideanDistance(v1, v2):
	"""
	Return the euclidean distance between vectors
	:param v1: a vector of numbers represented as a list
	:param v2: a vector of numbers represented as a list
	:return: the float value that is the Euclidean distance between v1 and v2
	Examples:
	>>> euclideanDistance([3, 1], [6, 5])
	5
	>>> euclideanDistance([0, 0], [3, 4])
	5
	"""
	dist_sum = 0
	distance = 0
	for i in range(len(v1)):
		dist_sum += (v2[i]- v1[i])**2
	distance = (dist_sum) ** 0.5

#	print(distance)
	return distance

def normalizeVector(v):
	"""
	Return a new vector that is vector v normalized
	:param v: a vector of numbers represented as a list
	:return: a new vector equivalent to v scaled to length 1 (ie: a unit vector)
	Example:
	>>> normalizeVector([6, 8])
	[.6, .8]
	"""
	normalized_vec = []
	path_dis = 0

	for i in range(len(v)):
		path_dis += (v[i])**2
	norm_path_dis = (path_dis) ** 0.5

	for j in range(len(v)):
		normalized_vec.append(v[j]/norm_path_dis)

#	print(normalized_vec)
	return normalized_vec


if __name__ == '__main__':
	#main()
	test_suite()