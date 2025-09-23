# Problem: Two Sum (Leetcode #1)
# Category: Arrays / Hash Map
# Time Complexcity: O(n)
# Space Complexcity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash_map:
                return [hash_map[diff], i] #hash_map[2]
            hash_map[n] = i

        return {}        
