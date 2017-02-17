
def find_max_crossing_subarray(A, low, mid, high):
	left_sum = -10000000
	summ = 0
	for i in range(mid,low-1,-1):
		summ = summ + A[i]
		if summ > left_sum:
			left_sum = summ
			max_left = i
	right_sum = -20000000
	summ = 0
	for j in range(mid+1, high +1):
		summ = summ + A[j]
		if summ>right_sum:
			right_sum = summ
			max_right = j
	return (max_left+1, max_right+1,left_sum + right_sum)

def find_max_subarray(A, low, high):
	if low == high:
		return (low, high, A[low])
	else:
		mid = (low + high)/2
		(left_low, left_high, left_sum) = find_max_subarray(A, low, mid)
		(right_low, right_high, right_sum) = find_max_subarray(A, mid + 1, high)
		(crossing_low, crossing_high, crossing_sum) = find_max_crossing_subarray(A,low, mid, high)
		if left_sum >= right_sum and left_sum >= crossing_sum:
			return (left_low, left_high, left_sum)
		elif right_sum >= left_sum and right_sum >= crossing_sum:
			return (right_low, right_high, right_sum)
		else:
			return (crossing_low, crossing_high, crossing_sum)

A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-22,15,-4,7]

(s,e,summ) = find_max_subarray(A,0,len(A) -1)

print s,e,summ