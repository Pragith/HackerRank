#	Range Minimum Query
#	https://www.hackerrank.com/contests/hindley-milner-feb14/challenges/range-minimum-query

inp = raw_input()

arr_len = int(inp.split(" ")[0])
cases = int(inp.split(" ")[1])

arr = raw_input()
arr = arr.split(" ")
#arr = [10,20,30,40,11,22,33,44,15,5]

for case in range(cases):
	ranges = raw_input()
	ranges = ranges.split(" ")

	a = []

	for i in range(int(ranges[0]),int(ranges[1])+1):
		a.append(int(arr[i]))

	#print a
	print min(a)