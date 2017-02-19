INT_MIN = -32000

def cut_rod(a, n):
	val = [0]*(n)

	val[0] = 0

	for i in range(1, n+1):
		max_value = INT_MIN
		for j in range(i):
			max_value = max(max_value, val[j] + a[i - j - 1])
		val[i] = max_value
	return val[n]





