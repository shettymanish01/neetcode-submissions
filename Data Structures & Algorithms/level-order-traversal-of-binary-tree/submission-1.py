# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root:
            return res
        stack = [root]
        while stack:
            temp = []
            temp_stack = []
            for item in stack:
                
                temp.append(item.val)
                if item.left:
                    temp_stack.append(item.left)
                if item.right:
                    temp_stack.append(item.right)
            res.append(temp)
            stack = temp_stack
        return res

