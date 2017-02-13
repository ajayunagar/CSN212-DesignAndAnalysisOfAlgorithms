#This program implement heap sort

#To heapify subtree rooted at index i.
#n = size of the heap
def heapify(arr, n, i):
	largest = i
	l = 2*i + 1
	r = 2*i + 2

	if l < n and arr[l] > arr[largest]:
		largest = l

	if r < n and arr[r] > arr[largest]:
		largest = r

	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, n, largest)

def heapSort(arr):
	#size of an array = n
	n = len(arr)

	#Build a max heap
	for i in range(n/2 -1, -1, -1):
		heapify(arr, n, i)

	#One by one extract largest element
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, i, 0)

if __name__ == "__main__":
	inputArray = []
	lenArray = int(raw_input("Length of an array"))
	for i in range(lenArray):
		x = int(raw_input("Element of an array:"))
		inputArray.append(x)
	print inputArray
	heapSort(inputArray)
	print inputArray