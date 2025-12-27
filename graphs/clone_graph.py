# Problem: Clone Graph
# Approach: Use DFS with a hashmap (original → clone). Clone each node once and reuse stored clones to avoid infinite cycles.
# Time Complexity:O(n)
# Space Complexity: O(n)

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None