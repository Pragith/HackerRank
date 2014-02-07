#	nCr
#	https://www.hackerrank.com/challenges/ncr

import operator as op

def nCr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom


cases = input()

for i in range(cases):
	inp = raw_input()
	inp = inp.split(" ")
	n = int(inp[0])
	r = int(inp[1])
	print nCr(n,r) % 142857