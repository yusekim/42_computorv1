class Term: # 항
	def __init__(self, exponent, coefficient):
		self.exponent = exponent # 차수
		self.coefficient = coefficient # 계수
	def __str__(self):
		return f"{self.coefficient} * X^{self.exponent}"

class Polynomial: # 다항식
	def __init__(self, terms):
		pass
