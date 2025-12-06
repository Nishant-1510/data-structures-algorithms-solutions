# Problem: Find Peak Element
# Approach: Use binary search on slopes - if the right neighbor is higher, move right; otherwise move left.
# Time Complexity:O(log n)
# Space Complexity: O(1)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            # left neighbor greater
            if nums[m] < nums[m + 1]:
                l = m + 1
            # right neighbor greater   
            else:
                r = m
        return l