#	nCr
#	https://www.hackerrank.com/challenges/ncr

from operator import mul
from fractions import Fraction

cases = input()

for i in range(cases):
	inp = raw_input()
	inp = inp.split(" ")
	n = int(inp[0])
	r = int(inp[1])
	print int( reduce(mul, (Fraction(n-i, i+1) for i in range(r)), 1) ) % 142857