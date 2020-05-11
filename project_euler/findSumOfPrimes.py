#NOTE
#1. using list to store previous primes
#2. using sqrt function drastically reduces the complexity
#TO Do:
# 1. Need to find optimal solution as at present this solution takes around 10 seconds for 2 million

import math
primeList = []

def isPrime(num):
    if num == 2:
        primeList.append(num)
        return True
    else:
        for p in primeList:
            # print p
            if p >= math.sqrt(num)+1:
                break
            if num % p == 0:
                return False
    primeList.append(num)
    # print primeList
    return True

def sumOfPrimes(limit):
    sum = 0
    for i in range(2, limit+1):
        if isPrime(i):
            sum = sum + i
            # print sum
    return sum
    # print primeList

if __name__ == '__main__':
    print(sumOfPrimes(2000000))
    # print(isPrime(2000000))

