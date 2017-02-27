
def LCS(a1, a2):

	m = len(a1)
	n = len(a2)

	dp = [[None]*(n+1) for i in range(m+1)]

	for i in range(m+1):
		for j in range(n+1):

			if i == 0 or j == 0:
				dp[i][j] = 0

			elif a1[i-1] == a2[i-1]:
				dp[i][j] = dp[i-1][j-1] + 1

			else:
				dp[i][j] = max(dp[i][j-1], dp[i-1][j])

	index = dp[m][n]

	lcs = [""]*(index + 1)

	lcs[index] = "\0"

	i = m
	j = n

	while i > 0 and j > 0:

		if a1[i-1] == a2[j-1]:
			lcs[index - 1] = a1[i-1]
			i = i - 1
			j = j - 1

		elif dp[i-1][j] > dp[i][j-1]:
			i = i - 1

		else:
			j = j - 1

	return lcs, index

if __name__ == '__main__':
	a1 = [1,2,3,4,5,6,7,8]
	a2 = [4,5,6,7,1,3,4,8]

	print LCS(a1,a2)


