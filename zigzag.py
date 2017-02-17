#using find_longest_subsequence() you can find longest
#continuous subsequence of any sequence
#Problems is solved by dividing them into many sub-
#problems, so this is a kind of DP problem.


#this function finds 1st zigzag sequence
#in sequence a and returns length of it and
#index where it ends.
def find_first_zigzag_length(a):
	l = 1	#initializing length
	i = 2	#starting at index = 2
	while(i < len(a) and (a[i]-a[i-1])*(a[i-1]-a[i-2]) < 0):	
		#checks if two difference are opposite or not!
		l = l + 1
		i = i+1
	return i-1,l


#This function calls find_first_zigzag_length() every
#time and get the longest common one.
def find_longest_subsequence(a):
	maximum_len = 0	#initializing max length
	j = 0
	while(j < len(a)-1):
		k, maximum_len = find_first_zigzag_length(a[j:])
		j = j+k
	return maximum_len

a = [1,17,5,10,13,15,10,5,16,8]

ml = find_longest_subsequence(a)
print ml

