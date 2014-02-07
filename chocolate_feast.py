cases = input()
#cases = 1

for i in range(cases):
	case = raw_input()
	#case = "58 6 3"
	case = case.split(" ")

	bill = int(case[0])
	price = int(case[1])
	wrappers = int(case[2])

	No_of_chocolate = bill / price
	balance_wrappers = No_of_chocolate

	while True:
		bal = balance_wrappers / wrappers
		Wrappers_Rem = balance_wrappers // wrappers
		No_of_chocolate = No_of_chocolate + bal
		balance_wrappers = bal + Wrappers_Rem
		if (balance_wrappers <= wrappers):
			if (balance_wrappers == wrappers):
				print No_of_chocolate + 1
			else:
				print No_of_chocolate
			break;




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

'''
Sub ab()

'dim bill as Integer, price as Integer, wrappers as Integer

    bill = 56
    Price = 8
    wrappers = 3
    balance_wrappers = 0
    
    Dim No_of_chocolate As Integer
    Dim bal As Integer
    
    No_of_chocolate = bill / Price
    balance_wrappers = No_of_chocolate
    Do Until balance_wrappers < wrappers
        bal = balance_wrappers / wrappers
        Wrappers_Rem = balance_wrappers Mod wrappers
        No_of_chocolate = No_of_chocolate + bal
        balance_wrappers = bal + Wrappers_Rem
     Loop
    MsgBox No_of_chocolate
End Sub

'''

'''
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