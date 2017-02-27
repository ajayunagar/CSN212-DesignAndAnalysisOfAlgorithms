def pos(dp, l, r, key):
	while r-l > 1:
		m = l + (r-l)/2
		if(dp[m] >= key):
			r = m
		else:
			l = m
	return r

def lcis(arr):
	n = len(arr)
	dp = [0]*10001
	dp[0] = arr[0]
	length = 1

	for i in range(1,n):
		if a[i] < dp[0]:
			dp[0] = a[i]
		elif a[i] > dp[length - 1]:
			dp[length] = a[i]
			length = length+1
		else:
			dp[pos(dp, -1, length-1,a[i])] = a[i]

	return length

a = [4,8,6,1,5,2]
p = lcis(a)
print p