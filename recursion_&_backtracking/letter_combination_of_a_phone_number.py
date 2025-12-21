# Problem: letter Combination of a Phone Number
# Approach: perform dfs by mapping each digit to letters and building combinations character by character.
# Time Complexity: O(n * 4^n)
# Space Complexity: O(n)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = { "2" : "abc",
                   "3" : "def",
                   "4" : "ghi",
                   "5" : "jkl",
                   "6" : "mno",
                   "7" : "qprs",
                   "8" : "tuv",
                   "9" : "wxyz" }
                   
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")
        
        return res