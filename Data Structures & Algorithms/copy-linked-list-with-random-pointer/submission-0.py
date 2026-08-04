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
        oldToNew = {None:None}
        dummy = head

        while dummy:
            copy = Node(dummy.val)
            oldToNew[dummy] = copy
            dummy = dummy.next

        dummy = head
        while dummy:
            copy = oldToNew[dummy]
            copy.next = oldToNew[dummy.next]
            copy.random = oldToNew[dummy.random]
            dummy = dummy.next

        return oldToNew[head]