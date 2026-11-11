class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # I would solve this usign binary search 
        
        # iterate through all the index of the array
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            diff = target - numbers[i]
            while l <= r:
                mid = l + (r - l) // 2

                if numbers[mid] == diff:
                    return [i + 1, mid + 1]
                elif numbers[mid] < diff:
                    l = mid + 1
                else:
                    r = mid -1
        return []
