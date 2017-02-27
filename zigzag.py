#using longest_zigzag() you can find longest
#subsequence of any sequence seq.
"""
len(zigzag[j]) = {1  if j = 0
				  2  if j == 1
				  len(zigzag[j-1])+ 1 if condition satisfies
				  len(zigzag[j-1]) if not}
"""
#Problems is solved by dividing them into many sub-
#problems, so this is a kind of DP problem.


"""
Here zigzag stores all the elements of
zigzag found so far
at every point we check if adding new
element to zigzag satisfies zigzag property
or not!
So, we keep updating zigzag every time.
So, we are not solving all the sub-
problems at every step but keep using previous
solution to find the current. So, this DP is
optimal.
"""

zigzag = []

def longest_zigzag(seq):
	n = len(seq)

	for j in range(n):
		if len(zigzag) == 0:
			zigzag.append(seq[j])
		elif len(zigzag) == 1:
			if seq[j] != zigzag[0]:
				zigzag.append(seq[j])
			else:
				continue
		else:
			if (seq[j] - zigzag[len(zigzag) - 1])* \
				(zigzag[len(zigzag) - 1] - zigzag[len(zigzag) - 2]) < 0 :
				zigzag.append(seq[j])
			else:
				continue
	return len(zigzag), zigzag



a = [1,17,5,10,13,15,10,5,16,8]

ml = longest_zigzag(a)
print ml
