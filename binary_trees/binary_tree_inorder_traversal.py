# Problem: Binary Trees Inorder Traversal
# Approach: Use DFS recursion to traverse the tree in Left → Root → Right order by processing left subtree, current node, then right subtree.
# Time Complexity:O(n)
# Space Complexity: O(n)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res