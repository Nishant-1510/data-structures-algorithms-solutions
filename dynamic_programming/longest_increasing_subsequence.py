# Problem: Longest Increasing Subsequence(LIS)
# Approach: Use DP where each index stores the LIS ending there by comparing with all previous elements
# Time Complexity:O(n ^ 2)
# Space Complexity: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
        