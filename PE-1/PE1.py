#Number Setup
minNum = 0
maxNum = 1000
currentNum = 0
div1 = 3
div2 = 5

#Track total matches, and a list to hold them
totalNumber = 0
numberList = [0, 0]

while currentNum < maxNum:
    if ((currentNum % div1 == 0) or (currentNum % div2 == 0)):
        totalNumber = totalNumber + 1
        numberList.append(currentNum)
    currentNum = currentNum + 1
    print("Test1")

print(totalNumber)
print(*numberList)

nSum = 0
for i in numberList:
    nSum = nSum + i

print(nSum)

while True:
    print