"""
Sorting is very basic problem in Computer Science and every class
on Algorithms generally start with Sorting. So, Here I've shared
my approach for some of the sorting algorithms.
"""


"""
1. Selection Sort:
This is "in-place" algorithm. So, you don't need extra space.
But average and worst running time of this Algorithm is O(n2), so we need to 
consider this as well.
"""

def selectionSort(A):
	print "running selection sort"
	if len(A) == 1:			#Checking for trivial case
		return A
	i = 1
	while(i < len(A)):
		if A[i-1] > A[i]:
			i+=1
			continue
		else:
			pivot = A[i]
			print i
			j = i-1;
			while (pivot > A[j] and j >= 0):
				A[j+1] = A[j]
				j=j-1

			A[j+1] = pivot
			i+=1
	return A

"""
2. Merge Sort:
---> This is divide and conquer Algorithm. It divide
main problem in many subproblems (in our case 2) and then
solve these problems recursively. 
"""
def merge(arr, l, m, r):
	n1= m - l + 1
	n2 = r - m

	L = [0]*(n1)
	R = [0]*(n2)

	for i in range(0, n1):
		L[i] = arr[l + i]

	for i in range(0, n2):
		R[j] = arr[m + 1 + j]

	i = 0
	j = 0
	k = l

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[i]
			j += 1
		k += 1

def mergeSort(arr, l, r):
	print "This is mergeSort"
	if l < r:
		m = (l + (r-1))/2
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)

"""
3. Quick Sort:
---> This algorithm in "in-place" and based on divide and conquer
approach. So, doesn't require extra space and average case 
running time is O(nlogn).
"""

def partition(arr, low, high):
	i = low - 1
	pivot = arr[high]

	for j in range(low, high):

		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

def quickSort(arr, low, high):
	print "This is quickSort"
	if low < high:
		pi = partition(arr, low, high)

		quickSort(arr, low, pi - 1)
		quickSort(arr, pi+1, high)

#main function
if __name__ == "__main__":
	inputArray = []
	lenArray = int(raw_input("Length of an array"))
	for i in range(lenArray):
		x = int(raw_input("Element of an array:"))
		inputArray.append(x)
	print inputArray
	sortedArray = selectionSort(inputArray)
	print sortedArray
