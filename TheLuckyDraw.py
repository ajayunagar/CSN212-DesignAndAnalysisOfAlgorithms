"""
Assignment 2, problem 3
problem statement:
https://www.codechef.com/problems/D2/
"""

#How this is different from traditional lis?
"""
We'll manage two lis in this.
one eding at a[i] and one starting from a[i]
also, we'll manage starting value for lis
ending at a[i] and ending value for lis starting
from a[i]
this way we can circular traverse the array
"""

def lcis(a):
	n = len(a)

	lis_e = [1]*n	#lis ending at a[i], with a[i] as its last element
	lis_s = [1]*n	#lis stanrting at a[i], with a[i] as first element

	lis_e_s = [None]*n   #save starting index of lis ending at i
	lis_s_e = [None]*n   #save ending index of lis starting at i

	lis_e_s[0] = a[0]
	lis_s_e[n-1] = a[n-1]

	for i in range(1,n):
		for j in range(0,i):
			if a[i] > a[j] and lis_e[i] < lis_e[j]+1:
				lis_e[i] = lis_e[j] + 1
				lis_e_s[i] = lis_e_s[j]
		if lis_e_s[i] == None:
			lis_e_s[i] = a[i]

	for i in range(n-2,-1,-1):
		for j in range(i+1,n):
			if a[i] < a[j] and lis_s[i] < lis_s[j] + 1:
				lis_s[i] = lis_s[j] + 1
				lis_s_e[i] = lis_s_e[j]
		if lis_s_e[i] == None:
			lis_s_e[i] = a[i]
	maximum = 1

	for i in range(0,n):
		if(lis_e_s[i%n] < lis_s_e[(i+1)%n]):
			a = lis_e[i%n] + lis_s[(i+1)%n]
			if a > maximum:
				maximum = a
	return maximum

if __name__ == '__main__':
	cases = int(raw_input())
	for i in range(cases):
		l = int(raw_input())
		numbers = raw_input()
		numbers = numbers.split(' ')
		a = [int(x.strip()) for x in numbers]
		print lcis(a)