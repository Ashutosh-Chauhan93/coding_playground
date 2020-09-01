
def sumSqDiff(limit):
    sum = 0
    sumSq = 0
    for i in range(1,limit+1):
        sum = sum + i
        #print(i^2)
        sumSq=sumSq+i**2
    print(sum, sumSq)
    Diff=sum**2-sumSq
    return Diff

if __name__=='__main__':
    print(sumSqDiff(100))
