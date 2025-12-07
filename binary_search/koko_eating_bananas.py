# Problem: Koko Eating Bananas
# Approach: Find the minimum speed k using monotonic condition.
# Time Complexity:O(N*log(max(p)))
# Space Complexity: O(1)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
                
        return res        