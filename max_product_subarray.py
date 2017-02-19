
def max_product_subarray(A):
	n = len(A)

	max_end = 1
	min_end = 1
	max_so_far = 1

	start = 0
	end = 0
	s = 0

	for i in xrange(0,n):

		if A[i] > 0:
			max_end  = max(max_end, max_end*A[i])
