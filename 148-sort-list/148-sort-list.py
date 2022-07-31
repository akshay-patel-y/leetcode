# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        a = []
        
        start = head
        
        while start:
            a.append(start.val)
            start = start.next
        a.sort()
        
        prev = head
        for i in a:
            prev.val = i
            prev = prev.next
        return head