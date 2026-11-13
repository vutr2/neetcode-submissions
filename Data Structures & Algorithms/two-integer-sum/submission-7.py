class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #because the arrays are unsorted so we cannot use two pointer here. 
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

         
