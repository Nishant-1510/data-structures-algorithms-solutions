# Problem: Validate Binary Search Tree
# Approach: Recursively validate each node by enforcing strict min–max bounds derived from ancestors.
# Time Complexity:O(n)
# Space Complexity: O(n)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if not node:
                return True

            if not (node.val < right and node.val > left):
                return False

            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))
        return valid(root, float("-inf"), float("inf"))