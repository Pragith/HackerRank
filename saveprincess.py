#	Bot saves Princess
#	https://www.hackerrank.com/challenges/saveprincess

def getDirection(before,after):
	if (after[0]<before[0] and after[1]==before[1]):
		return "UP"
	if (after[0]>before[0] and after[1]==before[1]):
		return "DOWN"
	if (after[0]==before[0] and after[1]<before[1]):
		return "LEFT"
	if (after[0]==before[0] and after[1]>before[1]):
		return "RIGHT"

##################### Logic #####################
def getSteps(p,m):

	x = p[0]
	y = p[1]

	a = m[0]
	b = m[1]

	if (b > y):
		before = [a,b]
		b -= 1
		after = [a,b]
		while (b >= y):		
			print getDirection(before,after)
			b -= 1
		if (a > x):
			b += 1
			before = [a,b]
			a -= 1
			after = [a,b]
			while (a >= x):			
				print getDirection(before,after)
				a -= 1
		elif (a < x):
			b += 1
			before = [a,b]
			a += 1
			while (a <= x):			
				after = [a,b]
				print getDirection(before,after)
				a += 1

	elif (b < y):
		before = [a,b]
		b += 1
		after = [a,b]
		while (b <= y):		
			print getDirection(before,after)
			b += 1
		if (a > x):
			b += 1
			before = [a,b]
			a -= 1
			after = [a,b]
			while (a >= x):			
				print getDirection(before,after)
				a -= 1
		elif (a < x):
			b += 1
			before = [a,b]
			a += 1
			after = [a,b]
			while (a <= x):			
				print getDirection(before,after)
				a += 1


##########################################



def displayPathtoPrincess(n,grid):
	a = x = 0
	for g in grid:
		b = g.find('m')
		if (b != -1):
			break;
		else:
			a += 1
	for g in grid:
		y = g.find('p')
		if (y != -1):
			break;
		else:
			x += 1
	p = [x,y]
	m = [a,b]

	getSteps(p,m)


m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)