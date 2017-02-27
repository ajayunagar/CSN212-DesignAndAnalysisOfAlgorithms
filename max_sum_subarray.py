import sys
INT_MIN = -32000

def max_sum_subarray(A):
	n = len(A)

	max_end = 0
	max_so_far = 0

	start = 0
	end = 0
	temp = 0

	for i in range(n):
		max_end = max_end + A[i]

		if max_so_far < max_end:
			max_so_far = max_end
			start = temp
			end = i

		if max_end < 0:
			max_end = 0
			temp = i+1
	return start,end,max_so_far

if __name__ == '__main__':
	A = [1,-2,3,-5,-4,12,-4,8,-9,-10]

	start,end,max_sum = max_sum_subarray(A)

	print start, end, max_sum


