# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ret = []
        
        while head:
            ret.append(head)
            head = head.next
            
        i = len(ret) - n
        ret = ret[:i] + ret[i+1:]
        
        for i, x in enumerate(ret):
            if (i+1) < len(ret):
                temp = ret[i]
                temp.next = ret[i+1]
                ret[i] = temp
            else:
                temp = ret[i]
                temp.next = None
                ret[i] = temp
                
        if not ret:
            return None
        return ret[0]
            
            
        