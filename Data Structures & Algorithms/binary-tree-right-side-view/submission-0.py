# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        stack = [root]
        while stack:
            level_val = None
            temp_stack = []
            for item in stack:
                if item:
                    level_val = item.val
                    temp_stack.append(item.left)
                    temp_stack.append(item.right)
            if level_val:
                res.append(level_val)
            stack = temp_stack

        return res