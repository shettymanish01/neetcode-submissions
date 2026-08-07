# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        lis = group_prev = dummy
        start = dummy.next

        limit = 0
        while lis:
            if limit == k:
                limit = 0
                kth = lis
                group_next = lis.next
                prev = lis.next
                # print(prev.val)
                # print(lis.next)
                while start != group_next:
                    # print(start.val, lis.next.val)
                    temp = start.next
                    start.next = prev
                    prev = start
                    start = temp
                # print("hereee")
                tmp = group_prev.next
                group_prev.next = kth
                group_prev = tmp
                lis = group_next
                limit += 1

            # print("here")
            lis = lis.next if lis else None
            limit += 1
            # print(lis.val)

        return dummy.next