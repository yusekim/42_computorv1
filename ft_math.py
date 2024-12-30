def abs(input):
	return input if input > 0 else input * -1

def sqrt(input):
	x_n = input / 2
	x_n1 = 0.5 * (x_n + input / x_n)
	while abs(x_n - x_n1) > 1e-6:
		x_n = x_n1
		x_n1 = 0.5 * (x_n + input / x_n)
	return(x_n1)
