# Problem: Jump Game
# Approach: Greedily maintain the farthest reachable index and verify we never get stuck before reaching the end.
# Time Complexity:O(n)
# Space Complexity: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False