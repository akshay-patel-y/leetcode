"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return head
        
        ret = []
        og = []
        while head:
            temp = Node(head.val)
            og.append(head)
            if ret:
                ret[-1].next = temp
            ret.append(temp)
            head = head.next
        for i in range(len(ret)):
            if og[i].random in og:
                x = og.index(og[i].random)
                ret[i].random = ret[x]
            
                
        return ret[0]
                
                
            
        