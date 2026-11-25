# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = ListNode(0)
        curr = dummy.next
        
        
        add = 0
        while l1 or l2:
            
            dit = l1.val + l2.val
            dit += add
            add = 0
            if dit <= 9:
                curr.val = dit
            else:
                add = 1
                dit -= 10
                curr.val = dit
            if l1.next == None and l2.next:
                l1.next = ListNode(0)
            elif l2.next == None and l1.next:
                l2.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next
            if l1 and l2:
                curr.next = ListNode(0)
                curr = curr.next
        if add >= 1:
            curr.next = ListNode(1)
        return dummy.next
        
        
        
            

        

        return dummy.next