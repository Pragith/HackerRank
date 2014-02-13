#	Encryption
#	https://www.hackerrank.com/challenges/encryption

import math

msg = "chillout"
msg = "feedthedog"
msg = "haveaniceday"

length = len(msg)

width = int(math.sqrt(length))
height = int(math.ceil(math.sqrt(length)))

if (width < height):
	rows = width
	cols = height
else:
	rows = height
	cols = width

print "Rows:",rows,"Columns:",cols




i = 0

for m in msg:
	if (i % cols == 0):
		print ''
	print m,
	i+=1	