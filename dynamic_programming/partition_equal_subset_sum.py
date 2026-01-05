# Problem: Partiton Equal Subset Sum.
# Approach: Transform into a 0/1 knapsack problem using dp to check if a subset with sum = total/2 exists.
# Time Complexity:O(n * sum(nums))
# Space Complexity: O(sum(nums))

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False 