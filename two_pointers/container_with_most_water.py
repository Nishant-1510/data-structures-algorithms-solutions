# Problem: Container With Most Water
# Approach: Use two pointers and always move the pointer at the shorter line to maximize area.
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return res