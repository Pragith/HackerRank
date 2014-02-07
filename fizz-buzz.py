#	FizzBuzz
#	https://www.hackerrank.com/challenges/fizzbuzz

for i in range(101):
    if i==0:
        continue
    elif i%15==0:
        print 'FizzBuzz'
    elif i%5==0:
        print 'Buzz'
    elif i%3==0:
        print 'Fizz'
    else:
        print i

# for i in range(1,101):print"Fizz"*(i%3<1)+"Buzz"*(i%5<1)or i
# for x in range(100): print x%3/2*'Fizz'+x%5/4*'Buzz' or x+1
# print '\n'.join('Fizz'*(not i%3) + 'Buzz'*(not i%5) or str(i) for i in range(1, 101))
# for i in range(1,101):print"FizzBuzz"[i*i%3*4:8--i**4%5]or i
