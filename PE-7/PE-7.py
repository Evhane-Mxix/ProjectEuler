import math

xPrime = 10001
num = 1
i = 0
while i <= xPrime:
    stop = math.sqrt(num)
    x = 2
    isPrime = True
    while x <= stop:
        if num % x == 0:
            isPrime = False
        x += 1
        if isPrime == False:
            x = stop + 1
    if isPrime:
        print(num)
        i += 1
    num += 1
while True:
    print