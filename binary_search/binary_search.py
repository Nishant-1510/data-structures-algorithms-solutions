# Problem: Binary Search
# Appoarch: Use the two-pointer technique (l and r) to repeatedly halve the search space by comparing the target with the middle element.
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1
