#factorial with memoization

memory = {}
def memoize_factorial(f):
	
	def inner(num):
		if num not in memory:
			memory[num] = f(num)
			print('result saved')
		else:
			print('returning result from saved memory')
		return memory[num]

	return inner
	
@memoize_factorial
def facto(num):
	if num == 1:
		return 1
	else:
		return num * facto(num-1)

print(facto(9))
print(facto(9))
