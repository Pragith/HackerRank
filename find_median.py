#	Find the Median
#	https://www.hackerrank.com/challenges/find-median

#arr = "0 1 2 4 6 5 3"
x = input()
arr = raw_input()

arr = arr.split(" ")
#arr = [13, 18, 13, 14, 13, 16, 14, 21, 13]
arr = sorted(arr)

print int(arr[(len(arr)/2)])
