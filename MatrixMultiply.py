#Matrix Multiplication
import time

#1. Naive Approach
def naiveMultiply(A, B):

	assert len(A[0]) == len(B)
	C = []
	for i in range(len(A)):
		cc = []
		for k in range(len(B[0])):
			e = 0
			for j in range(len(A[0])):
				e = e + A[i][j]*B[j][k]
			cc.append(e)
		C.append(cc)

	return C

#Strassent Algorithm

def strassenMultiply(A, B):

	assert len(A[0]) == len(B)	#dimension mismatch

	C = []
	for i in range(len(A)):
		cc = []
		for j in range(len(B[0])):
			cc.append(0)
		C.append(cc)

	r1 = 1
	if len(A) >= 2:
		r1 = len(A)/2

	c1 = 1
	if len(A[0]) >= 2:
		c1 = len(A[0])/2

	c2 = 1
	if len(B[0]) >= 2:
		c2 = len(B[0])/2

	a11 = []
	a12 = []
	a21 = []
	a22 = []
	b11 = []
	b12 = []
	b21 = []
	b22 = []

	



if __name__ == '__main__':
	A = [[1,2],[3,4],[5,6]]
	B = [[4,3,1],[2,4,5]]
	t0 = time.time()
	C = naiveMultiply(A,B)
	t = time.time() - t0
	print C, t