#	Help Mike
#	https://www.hackerrank.com/challenges/help-mike

cases = input()
#cases = 1

for case in range(cases):

	case = raw_input()
	#case = "10 4"
	case = case.split(" ")

	n = int(case[0])
	k = int(case[1])

	#arr = []
	count = 0


	for i in xrange(1,n+1):
		for j in xrange(i,n+1):
			if ((i+j) % k == 0 and i < j ):
				count += 1
				print [i,j],
				#arr.append(str(sorted([i,j])))
				#arr.append(sorted([i,j])) #### If this is used, then uncomment the lines below
	
	print count

	#print len(set(arr))	
	#print len(sorted(set(arr)))

'''
	#Removing duplicate sets:-
	for a in arr:
		print a
		x = int (str(a[0]) + str(a[1]))
		z.append(x)

	print len(sorted(set(z)))
'''