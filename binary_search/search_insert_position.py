# Problem: Search Insert Position
# Appoarch: Use binary search to find the first index where nums[mid] >= target. If the target is found, return its index. Otherwise, return the position where it would be inserted.
# Time Complexity:O(logn)
# Space Complexity: O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1        
        
        return l
        