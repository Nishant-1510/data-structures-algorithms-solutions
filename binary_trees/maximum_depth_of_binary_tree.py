# Problem: Maximum Depth of Binary Tree
# Approach: Recursively compute the depth of left and right subtrees and return 1 + max(leftDepth, rightDepth).
# Time Complexity:O(n)
# Space Complexity: O(n)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))