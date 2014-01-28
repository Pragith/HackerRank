#	Mark and Toys
#	https://www.hackerrank.com/challenges/mark-and-toys

#items = 7
#money = 50
#prices = "1 12 5 111 200 1000 10".split(" ")
#prices = "1 20 40 45 60 70 80 100 150".split(" ")


inp = raw_input()
prices = raw_input()

inp = inp.split(" ")
prices = prices.split(" ")

items = int(inp[0])
money = int(inp[1])


prices = [ int(x) for x in prices]
prices = sorted(prices)

#print "Items with prices:", prices
prices = [ x for x in prices if x <= money]
#print "Items with prices under" , money , ": ", prices



items = []
total = i = 0


while (total <= money and i <= len(prices)-1):
	total += prices[i]
	if (total <= money):
		items.append(prices[i])		
		#print "Item considered:", items		
		#print "Money:", money
		#print "Total:", total	
		i += 1

#print "Total items: ",items
#print "Count of items: ",len(items)
print len(items)

