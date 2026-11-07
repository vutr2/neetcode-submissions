class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prefix = 1 
        for i in range(len(nums)):
            prefix *= nums[i]
            res[i] = prefix
        
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            suffix *= nums[1]
            res[i] = suffix
        return res