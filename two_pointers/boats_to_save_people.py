# Problem: Boats to Save People
# Approach: Sort weights and use two pointers to greedily pair lightest with heaviest under the limit.
# Time Complexity:O(n logn)
# Space Complexity: O(1)

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        res = 0 # boats
        l, r = 0, len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        return res