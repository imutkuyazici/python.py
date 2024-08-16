
def selectionSort(array):
	
	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, size):
			if array[j] < array[min_index]:
				min_index = j
		(array[ind], array[min]) = (array[min_index], array[ind])
		print(arr)
arr = [6,5,4,3,2,1,2,3,4,5,6,8,9,0,5,3]
size = len(arr)
selectionSort(size)
print(' sıralaman bu sekilde : ')
print(arr)
