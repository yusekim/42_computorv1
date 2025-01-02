import ft_math

class Term: # 항
	def __init__(self, exponent, coefficient):
		self.exponent = exponent # 차수
		self.coefficient = coefficient # 계수

class Polynomial:
	def __init__(self, terms):
		self.terms = terms # Term 배열
		self.degree = terms[-1].exponent # 가장 큰 차수
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

	def calculate(self):
		if self.is_solution_is_real:
			print("All real number is a solution...")
			exit()
		self.is_calculatable()
		if self.degree == 1:
			self.calculate_oneD()
		elif self.degree == 2:
			self.calculate_twoD()

	def is_calculatable(self):
		for item in self.terms:
			if item.exponent > 2:
				print("The polynomial degree is strictly greater than 2, I can't solve.")
				exit()
			elif item.exponent != int(item.exponent) or item.exponent < 0:
				print("Unexpected polynomial degree detected, I can't solve.")
				exit()

	def calculate_twoD(self):
		a = self.terms[2].coefficient
		b = self.terms[1].coefficient
		c = self.terms[0].coefficient
		D = b * b - 4 * a * c
		if D > 0:
			print("Discriminant is strictly positive, the two solutions are:")
			ans1 = (-b - ft_math.sqrt(D)) / (2 * a)
			ans2 = (-b + ft_math.sqrt(D)) / (2 * a)
			print(round(ans1, 6), round(ans2, 6), sep="\n")
		elif D < 0:
			print("Discriminant is strictly negative, I can't solve.")
			exit()
		else:
			print("Discriminant is strictly zero, the solution is:")
			print(-b / 2 *a)


	def calculate_oneD(self):
		solution = self.terms[0].coefficient / self.terms[-1].coefficient * -1
		print("The solution is:", solution, sep='\n')

	@staticmethod
	def format_term(coefficient, exponent):
		coef_str = str(int(coefficient) if coefficient == int(coefficient) else coefficient)
		expo_str = str(int(exponent) if exponent == int(exponent) else exponent)
		return f"{coef_str} * X^{expo_str}"
