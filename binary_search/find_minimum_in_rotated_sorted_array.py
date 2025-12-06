# Problem: Find Minimum in Rotated Sorted Array.
# Appoarch: Use binary search to find the unsorted portion.If nums[mid] > nums[right], the minimum is in the right half; otherwise it is in the left half. Continue until left == right.
# Time complexity: O(log n)
# Space complexity: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res                