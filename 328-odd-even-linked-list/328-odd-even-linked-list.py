# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        evens = None
        odds = None
        ret = None
        evenHead = None
        curr = 0
        while head:
            if curr % 2 != 0:
                if evens:
                    evens.next = head
                    evens = evens.next
                else:
                    evens = head
                    evenHead = evens
            else:
                if odds:
                    odds.next = head
                    odds = odds.next
                else:
                    odds = head
                    ret = odds
            head = head.next
            curr += 1
        if evens and evens.next:
            evens.next = None
        odds.next = evenHead

        return ret
        