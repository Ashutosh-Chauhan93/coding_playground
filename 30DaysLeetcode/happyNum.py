def square(n):
    return n*n

def sumOfSquares(num):
    liNumStr = list(str(num))
    liSquare = list(map(square,list(map(int,liNumStr))))
    return sum(liSquare)

def happyNum(n):
    sumOfSq = sumOfSquares(n)

    if sumOfSq == 1:
        return True

    digits = [0,1,2,3,4,5,6,7,8,9]

    while sumOfSq != 1:
        if len(digits) == 0:
            break

        sumOfSq = sumOfSquares(sumOfSq)

        if sumOfSq == 1:
            return True

        liOfDigits = list(str(sumOfSq))
        liOfDigits = map(int, liOfDigits)
        for digit in liOfDigits:
            if digit in digits:
                digits.remove(digit)

    return False


if __name__=='__main__':
    print(happyNum(11))