# Problem: Binary Tree level Order Traversal
# Approach: Perform a breadth-first search using a queue to visit nodes level by level from left to right.
# Time Complexity:O(n)
# Space Complexity: O(n)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)
        
        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res