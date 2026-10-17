# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head        
        fast = head
        while fast and fast.next:
            slow = slow.next         
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None

        while second:
            nex = second.next
            second.next = prev
            prev = second
            second = nex
        
        first = head
        second = prev
        
        while second:
            temp = first.next       
            first.next = second     
            first = first.next      
            second = first.next     
            first.next = temp       
            first = first.next      

        return 
            
