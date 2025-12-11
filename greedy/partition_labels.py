# Problem: Partition Labels
# Approach: Track each character’s last occurrence and greedily cut a partition whenever the current index reaches the farthest last occurrence.
# Time Complexity:O(n)
# Space Complexity: O(1)

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i
        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        return res
        