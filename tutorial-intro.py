#	Intro to Tutorial Challenges
#	https://www.hackerrank.com/challenges/tutorial-intro

key = input()
size = input()

ar = raw_input().split(" ")
ar = [ int(x) for x in ar]

print ar.index(key)	