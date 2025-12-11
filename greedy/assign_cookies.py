# Problem: Assign Cookies
# Approach: Sort both arrays and greedily match each child with the smallest cookie that satisfies their greed.
# Time Complexity:O(n logn + m logm)
# Space Complexity: O(1)

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = j = 0
        while i < len(g):
            while j < len(s) and g[i] > s[j]:
                j += 1
            if j < len(s):
                i += 1
                j += 1
            else:
                break
        return i

        