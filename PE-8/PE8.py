inputNum = "66896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

#longSequences = []
"""
def SplitZero(inp, startIndex):
    index = startIndex
    cSequence = []
    cNum = int(inp[startIndex])
    while cNum != 0 and index < len(inp):
        cSequence.append(cNum)
        index += 1
        cNum = int(inp[index])
    #print(cSequence)
    if(len(cSequence) - 1) >= 13:
        longSequences.append(cSequence)
        print(cSequence)
    return index

i = 0
while i < len(inputNum):
    i = SplitZero(inputNum, i)

gSum = 0

for i in longSequences:
    end = len(i) - 1
    x = 0
    while x < end - 13:
        cSum = 1
        for y in range(x, (x + 13), 1):
            cSum *= i[y]
        if cSum > gSum:
            gSum = cSum
        x += 1

print(gSum)
"""

gProd = 0
for i in range(0, len(inputNum) - 14, 1):
    n = int(inputNum[i])
    x = i
    cProd = 1
    while x <= (i + 13):
        cProd *= int(inputNum[x + 1])
        x += 1
    if cProd > gProd:
        gProd = cProd
        print(inputNum[x-13:x])
        print(cProd)
print(gProd)

while True:
    print