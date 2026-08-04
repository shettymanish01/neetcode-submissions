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
                
                if item:
                    temp.append(item.val)
                    temp_stack.append(item.left)
                    temp_stack.append(item.right)
            if temp:
                res.append(temp)
            stack = temp_stack
        return res

