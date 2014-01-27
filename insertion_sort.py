#  Algorithms -> Sorting -> Insertion Sort - Part 1
#  https://www.hackerrank.com/challenges/insertionsort1

def insertionSort(ar):    
	length = len(ar)
	last_element = ar[-1]
	for i in range(length-1,-1,-1):
		if (last_element < ar[i]):
			ar[i+1] = ar[i]
			for n in ar:
				print n,
			print ''
			index = i
	ar[index] = last_element
	for n in ar:
		print n,


ar = [1,2,5,8,9,10,50,3]
#ar = [2,4,6,8,3]
insertionSort(ar)