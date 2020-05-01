def decimalTobinary(num):
    n= num
    strNum = str()
    while n > 0:
        r = n % 2
        strNum = strNum+str(r)
        n = n/2
    # strNum[::-1]
    print(strNum[::-1])
    bin = int(strNum[::-1], base=2)
    print (bin)
    print(binaryTodecimal(strNum[::-1]))


def binaryTodecimal(num):
    n = str(num)
    nList = list(n)
    power = 0
    decimal = 0
    for elem in nList[::-1]:
        decimal = decimal + int(elem)*(2**power)
        power = power + 1
    return decimal


if __name__=='__main__':
    decimalTobinary(125)

