# Problem: Search in Rotated Sorted Array
# Appoarch: Use modified binary search. At each step, check which half (left or right) is sorted. If the target lies inside the sorted half, move towards that half; otherwise move to the unsorted half.
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1


        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion        
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1                                