maxNum = 100
squareSum = 0
sumSquare = 0


for i in range(1, maxNum + 1):
    squareSum += i
    sumSquare += i ** 2
    print(squareSum)
squareSum = squareSum ** 2

diff = squareSum - sumSquare

print(diff)

while True:
    print