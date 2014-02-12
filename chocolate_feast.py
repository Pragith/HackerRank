#	Chocolate Feast
#	https://www.hackerrank.com/challenges/chocolate-feast

cases = input()
#cases = 1

for i in range(cases):
	case = raw_input()
	#case = "58 6 3"
	case = case.split(" ")

	bill = int(case[0])
	price = int(case[1])
	wrappers = int(case[2])

	total_Chocolates = bill / price
	w = total_Chocolates

	while w/wrappers:
		chocolates = w/wrappers
		w = w%wrappers + chocolates
		total_Chocolates += chocolates
	print total_Chocolates
