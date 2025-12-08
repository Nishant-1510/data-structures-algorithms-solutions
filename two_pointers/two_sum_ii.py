# Problem: Two Sum II - Input Array is Sorted
# Appoarch: Move left/right pointers inward depending on whether the sum is smaller or larger than the target.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []