import ft_math

class Term: # 항
	def __init__(self, exponent, coefficient):
		self.exponent = exponent # 차수
		self.coefficient = coefficient # 계수

class Polynomial:
	def __init__(self, terms):
		self.terms = terms # Term 배열
		self.degree = terms[-1].exponent # 가장 큰 차수
		self.is_unexpected_exponent = False # 음수 또는 소수 차수가 포함시 True
		self.is_solution_is_real = False # 해가 모든 실수일 경우 True

	def __str__(self):
		if not self.terms:
			self.is_solution_is_real = True
			return "0 = 0"
		equation = ""
		for idx, term in enumerate(self.terms):
			coefficient = term.coefficient
			exponent = term.exponent
			if (exponent < 0 or exponent != int(exponent)):
				self.is_unexpected_exponent = True
			if idx == 0:
				equation += f"{self.format_term(coefficient, exponent)}"
			else:
				if coefficient > 0:
					equation += f" + {self.format_term(coefficient, exponent)}"
				else:
					equation += f" - {self.format_term(ft_math.abs(coefficient), exponent)}"

		return f"{equation} = 0"

	def print_degree(self):
		expo_str = str(int(self.degree) if self.degree == int(self.degree) else self.term[-1].exponent)
		print(f"Polynomial degree: {expo_str}")


	@staticmethod
	def format_term(coefficient, exponent):
		coef_str = str(int(coefficient) if coefficient == int(coefficient) else coefficient)
		expo_str = str(int(exponent) if exponent == int(exponent) else exponent)
		return f"{coef_str} * X^{expo_str}"
