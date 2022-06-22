num = 100
product = 1

for i in range (1, num, 1): #num!
    product *= i
print(product)

digits = str(product)
total = 0
for i in range(0, len(digits), 1):
    total += int(digits[i])
print(total)
while True:
    print