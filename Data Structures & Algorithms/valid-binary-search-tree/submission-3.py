# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # stack = [[root, float('-inf'), float('inf')]]

        # while stack:
        #     temp = []
        #     for node, left, right in stack:
        #         if not (left < node.val < right):
        #             return False
        #         if node.left:
        #             temp.append([node.left, left, node.val ])
        #         if node.right:
        #             temp.append([node.right, node.val, right ])

        #     stack = temp
        # return True


        queue = deque([(root, float('-inf'), float('inf'))])

        while queue:
            node, left, right = queue.popleft()

            if not (left < node.val < right):
                return False
            if node.left:
                queue.append((node.left, left, node.val))
            if node.right:
                queue.append((node.right, node.val, right))

        return True

