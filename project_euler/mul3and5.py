def mul3and5(number):
    print number
    total = 0
    for n in range(number):
        if ((n % 3 == 0) or (n % 5 == 0)) is True:
            total = total + n
    return total


if __name__ == '__main__':
    num = 1000
    print ("Sum of multiples of 3 and 5 below {0} = {1}".format(num, mul3and5(num)))

#from temp branch

