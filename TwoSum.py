
def twoSum(nums, target):
    for i in range(len(nums)):
        cur = nums[i]
        dif = target - cur
        for count, n in enumerate(nums[i+1:], i+1):
            if n == dif:
                return [i, count]






print(twoSum([1, 2, 3, 4, 5, 6, 7, 8], 9))