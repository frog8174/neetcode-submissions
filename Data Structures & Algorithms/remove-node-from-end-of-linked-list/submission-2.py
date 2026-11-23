# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(-1)             

        nodes = []
        while head :
            nodes.append(head)
            head = head.next

        length = len(nodes)
        if n == length: return nodes[0].next
        else:
            nodes[length-n-1].next = nodes[length-n].next
            return nodes[0]
