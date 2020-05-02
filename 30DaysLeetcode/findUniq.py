def findUnique(nums):
    di = dict()
    nums = sorted(nums)
    lastElem = nums[0]
    di[lastElem] = 1
    for elem in nums[1::]:
        if elem != lastElem:
            di[elem]=1
            lastElem = elem
        else:
            di[elem] = di[elem]+1
    for key in di.keys():
        if di[key] == 1:
            return key

if __name__=='__main__':
    print(findUnique([2,1,2,1,3,4,1,4,2]))