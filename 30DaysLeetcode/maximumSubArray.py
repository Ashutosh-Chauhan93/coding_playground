def maxSubarray(arr):

    subArr1 = arr[:len(arr)-1:]
    subArr2 = arr[1::]
    sum1 = sum(subArr1)
    sum2 = sum(subArr2)
    if sum1 > sum2:
        arr = subArr1
        maxSum = sum1
        maxSubArr = subArr1
    else:
        arr = subArr2
        maxSum = sum2
        maxSubArr = subArr2
    subArr1 = arr[:len(arr) - 1:]
    subArr2 = arr[1::]

    while len(subArr1) != 1 or len(subArr2) != 1:
        sum1 = sum(subArr1)
        sum2 = sum(subArr2)
        if sum1 > sum2:
            arr = subArr1
            maxSum = sum1
            maxSubArr = subArr1
        else:
            arr = subArr2
            maxSum = sum2
            maxSubArr = subArr2
        subArr1 = arr[:len(arr)-1:]
        subArr2 = arr[1::]
