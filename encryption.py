#	Encryption
#	https://www.hackerrank.com/challenges/encryption

import math

msg = "chillout"
#msg = "feedthedog"
#msg = "haveaniceday"

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



def split_len(seq, length):
	return [seq[i:i+length] for i in range(0, len(seq), length)]

i = 0
arr = []

seq = 'chillout'
length = cols

for i in range(0, len(seq), length):
	print i,i+length,
	print seq[i:i+length]

for chunk in split_len(msg,cols):
	print ''
	#print chunk[1],





'''


i = 0


for m in msg:
	if (i % cols == 0):
		print ''
	print i,
	i += 1

print arr









i = 0
arr = []

for m in msg:
	if (i % cols == 0):
		print ''
		arr.append('')
	print m,
	arr.append(m)
	i+=1	

print arr


'''


