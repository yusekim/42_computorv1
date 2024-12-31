import modules
from shared import termList

def ft_is_number(s):
	try:
		float(s)  # float 변환 시도
		return True
	except ValueError:
		return False

def buildTerm(split):
	sign = False
	equal_sign = False
	exponent = 0
	coefficient = 0
	for i in range(len(split)):
		if ft_is_number(split[i]):
			coefficient = float(split[i])
			if sign ^ equal_sign:
				coefficient *= -1
			sign = False
		elif split[i] == '-':
			sign = True
		elif split[i] == '=':
			equal_sign = True
		elif split[i][0] == 'X':
			exponent = float(split[i][2:])
			termList.append(modules.Term(exponent, coefficient))

def symplify():
	i = 0
	while i < len(termList) - 1:
		if termList[i].exponent == termList[i + 1].exponent:
			termList[i + 1].coefficient += termList[i].coefficient
			termList.pop(i)
			if termList[i].coefficient == 0:
				termList.pop(i)
		else:
			i += 1
