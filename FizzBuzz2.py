print "Fizz buzz counting up to 100"

n=1

while n!=101:
    if n % 5 == 0 and n % 3 == 0:
        print "FizzBuzz"
        n+=1
    elif n % 3 == 0:
        print "Fizz"
        n+=1
    elif n % 5 == 0:
        print "Buzz"
        n+=1
    else:
        print n
        n+=1