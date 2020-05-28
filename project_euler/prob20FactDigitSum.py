def sumOfFacDigits(num):
    prod = 1
    sum = 0
    for i in range(num, 1, -1):
        prod = prod * i
    prodStrList = list(str(prod))
    for i in prodStrList:
        sum = sum + int(i)
    return sum

if __name__=='__main__':
    print(sumOfFacDigits(100))

