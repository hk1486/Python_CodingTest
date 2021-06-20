def FindBalance(nums):
    for i in range(len(nums)):
        if (sum(nums) - nums[i])%2 == 0:
            if sum(nums[0:i]) == sum(nums[i+1:]):
                return [i,nums[i],sum(nums[0:i])]
    return []
print(FindBalance([1,2,3,4,5,2,3,5]))