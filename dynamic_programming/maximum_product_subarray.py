# Problem: Maximum Product Subarray
# Approach: Track both maximum and minimum products ending at each index since a negative number can flip signs, updating the global maximum at every step.
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) 
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res

        dp = []
        