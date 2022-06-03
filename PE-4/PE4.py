def Palindromer(inputNum):
    inputString = str(inputNum)
    x = 0
    isPalindrome = True
    while x < len(inputString) / 2:
        if(inputString[x] != inputString[-(x+1)]):
            isPalindrome = False
        x = x + 1
    if isPalindrome:
        print(inputNum)
    
    return(isPalindrome)


num1 = 100
num2 = 100
hPal = 0
while num1 < 1000:
    num2 = 100
    while num2 < 1000:
        product = num1 * num2
        if Palindromer(product):
            if product > hPal:
                hPal = product
        num2 = num2 + 1
    num1 = num1 + 1
print(hPal)
while True:
    print
    
    