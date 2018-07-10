# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""
want = int(raw_input("How many numbers do you want in your Fibonacci sequence? "))
previousNumber=0
currentNumber=1
for i in range (want) :
    nextNumber = previousNumber + currentNumber
    print currentNumber
    previousNumber=currentNumber
    currentNumber=nextNumber

# powers of 2 extension

want=int(raw_input("How many powers of 2 would you like to see? "))
count =0
while count<want:
    print 2**count
    count+=1

# divisor extension

divisor=2
num=int(raw_input("What integer would you like all of the divisors for?"))
if num<1:
    print "Invalid range: please try again."
elif num==2:
    print "1"
    print "2"
else :
    print 1
    while divisor<num :
        if num%divisor==0:
            print divisor
        divisor+=1
    print num
