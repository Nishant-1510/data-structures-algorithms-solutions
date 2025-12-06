# Problem: First Bad Version
# Appoarch: Use binary search to find the earliest version where isBadVersion becomes true.
# Time Complexity:O(logn)
# Space Complexity: O(1)
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while l < r:
            m = l + (r - l) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1

        return l            