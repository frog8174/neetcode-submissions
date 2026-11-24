"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        maps = {}
        curr = head
        while curr:
            maps[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                maps[curr].next = maps[curr.next]
            
            if curr.random:
                maps[curr].random = maps[curr.random]
            curr = curr.next
            
        
       
        return maps[head]
         

