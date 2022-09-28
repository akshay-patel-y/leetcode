"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
                
        
        q, clones = deque([node]), {node.val: Node(node.val, [])}
        
        while q:
            curr = q.popleft()
            curr_clone = clones[curr.val]
            for j in curr.neighbors:
                if j.val not in clones:
                    clones[j.val] = Node(j.val, [])
                    q.append(j)
                curr_clone.neighbors.append(clones[j.val])
                
        return clones[node.val]
    


