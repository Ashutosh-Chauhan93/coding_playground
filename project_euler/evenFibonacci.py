def sumevenfib(limit):
    prev = 0
    curr = 1
    sumEven = 0
    while curr < limit:
        nxt = prev + curr
        prev = curr
        curr = nxt
        if curr % 2 == 0:
            print "EVEN curr = {0}".format(curr)
            sumEven = sumEven + curr
    return sumEven


if __name__ == '__main__':
    print sumevenfib(4000000)
