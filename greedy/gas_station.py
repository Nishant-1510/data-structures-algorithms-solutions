# Problem: Gas Station
# Approach: If the total gas is sufficient, the start index is where the cumulative tank first drops below zero while scanning.
# Time Complexity:O(n)
# Space Complexity: O(1)

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1

        return res