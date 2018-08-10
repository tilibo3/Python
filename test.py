def HeapSort(list):
	for i in range(len(list)//2-1, -1, -1):
		HeapAdjust(list, i, len(list)-1)
	for i in range(len(list)-1, 0, -1):
		list[0], list[i] = list[i], list[0]
		HeapAdjust(list, 0, i-1)

def HeapAdjust(list, s, m):
	tmp = list[s]
	j = 2 * s + 1
	while j <= m:
		if j < m and list[j] < list[j+1]:
			j = j + 1
		if tmp > list[j]:
			break
		list[s] = list[j]
		s = j
		j = j * 2 + 1
	list[s] = tmp

def Qsort(list, low, high):
	if low < high:
		pivotIndex = Partition(list, low, high)
		Qsort(list, low, pivotIndex-1)
		Qsort(list, pivotIndex+1, high)

def Partition(list, low, high):
	pivot = list[low]
	while low < high:
		while low < high and list[high] > pivot:
			high = high - 1
		list[low] = list[high]
		while low < high and list[low] <= pivot:
			low = low + 1
		list[high] = list[low]
	list[low] = pivot
	return low

def MergeSort(list):
	if len(list) <= 1:
		return list
	middle = len(list)//2
	left = MergeSort(list[:middle])
	right = MergeSort(list[middle:])
	return merge(left, right)

def merge(a, b):
	i, j = 0, 0
	c = []
	while i < len(a) and j < len(b):
		if a[i] < b[j]:
			c.append(a[i])
			i = i + 1
		else:
			c.append(b[j])
			j = j + 1
	while i < len(a):
		c.append(a[i])
		i = i + 1
	while j < len(b):
		c.append(b[j])
		j = j + 1
	return c

if __name__ == "__main__":
	alist1 = [50, 10, 90, 30, 70, 40, 80, 60, 20]
	HeapSort(alist1)

	alist2 = [50, 10, 90, 30, 70, 40, 80, 60, 20]
	Qsort(alist2, 0, len(alist2)-1)

	alist3 = [50, 10, 90, 30, 70, 40, 80, 60, 20]
	result = MergeSort(alist3)

	print ('<'.join(map(lambda x: str(x), alist1)))
	print ('<'.join(map(lambda x: str(x), alist2)))
	print ('<'.join(map(lambda x: str(x), result)))