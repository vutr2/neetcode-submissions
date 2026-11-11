class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # im gonna use hash set for this one. 

        #step one turn the array into set
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # try to find the number start the sequence. 
            if (num - 1) not in numSet:
                # if not in the set, the sequence start
                length = 1 
                #Start the while loop with the current number. 
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest