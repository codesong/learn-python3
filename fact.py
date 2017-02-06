# n <= 998

def fact(n):
	if n == 1:
		return 1
	else: 
		return n * fact(n - 1)


def fact(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if num = 1:
		return product
	else:
		return fact_iter(num - 1, n * product)