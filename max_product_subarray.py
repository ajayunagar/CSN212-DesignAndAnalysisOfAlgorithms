
def max_product_subarray(A):
	n = len(A)

	max_end = 1
	min_end = 1
	max_so_far = 1

	start = 0
	end = 0
	temp_start = 0
	temp_end = 0


	for i in xrange(0,n):

		if A[i] > 0:
			
			max_end = max_end*A[i]
			min_end = min(min_end*A[i], 1)

			if max_so_far < max_end:
				max_so_far = max_end
				end = i
				start = temp_start

		elif A[i] == 0:
			max_end = 1
			min_end = 1
			temp_start = i+1

		else:
			temp = max_end
			max_end = max(1, min_end*A[i])
			min_end = min(1, temp*A[i])

			if max_so_far < max_end:
				max_so_far = max_end
				start = temp_start
				end = i
	return max_so_far, start, end

if __name__ == '__main__':
	A = [-8, -5, 2, 0, 3, -4, -18, 5, -4, 4]
	max_product, start, end = max_product_subarray(A)
	print max_product, start, end





