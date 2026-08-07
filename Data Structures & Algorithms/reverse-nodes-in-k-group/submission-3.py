# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = group_prev = dummy
        start = dummy.next

        limit = 0
        while cur:
            if limit == k:
                limit = 0
                group_next = prev = cur.next
                # print(prev.val)
                # print(cur.next)
                while start != group_next:
                    # print(start.val, cur.next.val)
                    temp = start.next
                    start.next = prev
                    prev = start
                    start = temp
                # print("hereee")
                tmp = group_prev.next
                group_prev.next = prev
                group_prev = tmp
                cur = group_next
                limit += 1

            # print("here")
            cur = cur.next if cur else None
            limit += 1
            # print(cur.val)

        return dummy.next