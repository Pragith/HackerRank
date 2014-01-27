#cases = input()
cases = 1

for i in range(cases):
	#case = raw_input()
	case = "48 6 3"
	case = case.split(" ")

	bill = int(case[0])
	price = int(case[1])
	wrappers = int(case[2])

	chocolates = bill/price
	bal_wrap=chocolates

	total = 0
	if bal_wrap >= wrappers:
		balance=bal_wrap/wrappers
		total=chocolates+balance
	print total

'''
	if chocolates == exchange:
		total = chocolates + 1

	elif chocolates < exchange:
		total = chocolates

	elif chocolates > exchange:
		free_chocolates = chocolates % exchange
		balance = chocolates % exchange
		total = chocolates + free_chocolates
        
	print total
'''
