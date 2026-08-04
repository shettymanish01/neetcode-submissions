# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        prev = slow.next = None


        while second_half:
            tmp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = tmp

        l1 = head
        l2 = prev
        while l1 and l2:
            tmp1 = l1.next
            tmp2 = l2.next
            l1.next = l2
            l2.next = tmp1
            l2 = tmp2
            l1 = tmp1

        