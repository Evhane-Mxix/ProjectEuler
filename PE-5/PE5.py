factorList = []
larExp = []
maxNum = 20

for i in range(maxNum):
    larExp.append(0)


def primeFactors(inp):
    #get number of 2s
    print(inp)
    i = 2
    while i * i <= inp:
        if inp % i:
            i = i + 1
        else:
            inp = inp / i
            factorList.append(i)
    if inp > 1:
        factorList.append(int(inp))
    print(factorList)
    
def largestExponent():
    i = 1
    while i < maxNum:
        counter = 0
        big = 0
        for x in factorList:
            if x == i:
                counter += 1
            if x != i:
                if big < counter:
                    big = counter
                counter = 0
        larExp[i] = big
        i += 1



i = 1
while i <= maxNum:
    primeFactors(i)
    i += 1
largestExponent()
print(larExp)

x = 0
total = 1
for i in larExp:
    
    total *= x ** i
    x += 1
    
print(total)

while True:
    print