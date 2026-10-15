# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 創造一個哨兵節點 (值隨便填)，並且用 curr 變數當作「指標」去幫我們牽線
        dummy = ListNode(-1)
        curr = dummy
        
        # 2. 當兩邊都還有節點時，比較大小，把較小的接在 curr 後面
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1
        else:
            curr.next = list2
        
        return dummy.next


