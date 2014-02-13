#	Lonely Integer
#	https://www.hackerrank.com/challenges/lonely-integer

d = input()
arr = raw_input()
arr = arr.split(" ")
#arr = "0 0 1 2 1"

ans = []

for val in arr: 
	ans.append(arr.count(val))

print arr[[i for i,x in enumerate(ans) if x == 1][0]]

