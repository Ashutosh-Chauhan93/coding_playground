def checkPrime(num):
    # divcount = 0
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    # for i in range(2, (num/2)):
    i = 2
    while num > 1:
        if i > (num/2):
            return True
        if num % i == 0:
            return False
        i = i + 1
    return True

def findLargestPrimeFactor(num):
    loopCnt = 0
    divisor = 2
    orig = num
    lastSuccDiv = 1
    while num > 1 and divisor <= (orig/2):
        loopCnt = loopCnt + 1
        res = checkPrime(divisor)
        if res is True:
            if num % divisor == 0:
                lastSuccDiv = divisor
                num = num / divisor
                res2 = checkPrime(num)
                if res2 is True:
                    return num
        divisor = divisor+1
    return lastSuccDiv


if __name__ == '__main__':
    print findLargestPrimeFactor(600851475143)
    print findLargestPrimeFactor(27)
    print findLargestPrimeFactor(8)
    print findLargestPrimeFactor(13)
    # print checkPrime(8)
