#	Game of Thrones - I
#	https://www.hackerrank.com/challenges/game-of-thrones

import collections

'''
msg = "cdcdcdcdeeeef"
msg = "aaabbbb"
msg = "cdefghmnopqrstuvw"
'''
msg = raw_input()
msg = msg.lower()

even = odd = 0

letters = 'abcdefghijklmnopqrstuvwxyz1234567890'

d = collections.defaultdict(int)
for c in msg:
	if (c in letters):
		d[c] += 1


for c in d:
	if (c in letters):
		#print '%s %6d' % (c, d[c])
		if (d[c] % 2 == 0):
			even+=1
		else:
			odd+=1
	
if ((odd == 1 or odd == 0) and even >= 0):
	print "YES"
else:
	print "NO"