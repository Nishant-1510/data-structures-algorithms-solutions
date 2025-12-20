# Problem: Construct Binary Tree from Preorder and Inorder Traversal
# Approach: Use preorder to select roots and inorder indices to recursively split left and right subtrees.
# Time Complexity:O(n)
# Space Complexity: O(n)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root