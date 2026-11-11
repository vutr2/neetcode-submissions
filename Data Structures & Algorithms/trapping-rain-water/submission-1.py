class Solution:
    def trap(self, height: List[int]) -> int:
        # Step 1: Initialize two pointers at both ends of the array
        left = 0
        right = len(height) - 1

        # Step 2: Track the maximum height seen from each side
        left_max = 0
        right_max = 0

        # Step 3: Store the total trapped water
        water = 0

        # Step 4: Process bars until the two pointers meet
        while left < right:

            # Step 5: Process the side with the shorter current bar
            if height[left] < height[right]:

                # Step 6: Update the maximum height on the left
                if height[left] >= left_max:
                    left_max = height[left]

                # Step 7: Calculate trapped water at the left position
                else:
                    water += left_max - height[left]

                # Step 8: Move the left pointer forward
                left += 1

            else:

                # Step 9: Update the maximum height on the right
                if height[right] >= right_max:
                    right_max = height[right]

                # Step 10: Calculate trapped water at the right position
                else:
                    water += right_max - height[right]

                # Step 11: Move the right pointer backward
                right -= 1

        # Step 12: Return the total amount of trapped water
        return water


