

#Create fibonacci sequence
fibSeq = [1,2,3,5,8,13,21,34,55,89]
newNum = 0
while newNum < 4000000:
    newNum = fibSeq[-1] + fibSeq[-2]
    if newNum < 4000000:
        fibSeq.append(newNum)



#Get even numbers
evenFib = []
for i in fibSeq:
    if i % 2 == 0:
        evenFib.append(i)

#Sum even sequence
numSum = 0
for i in evenFib:
    numSum = numSum + i
    
print(numSum)
while True:
    print