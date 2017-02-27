INT_MIN = -32000

def cut_rod(a, n):
	val = [0]*(n+1)
	val[0] = 0
	
	s = [0]*(n+1)
	s[0] = 0

	for i in range(1, n+1):
		max_value = INT_MIN

		for j in range(i):

			if max_value <  val[j] + a[i - j - 1]:
				max_value = val[j] + a[i - j - 1]
				s[j] = i

		val[i] = max_value
	return val, s

prices = [0,1,5,8,10,13,17,18,22,25,30]

vl, s = cut_rod(prices , 11)
print vl, s





