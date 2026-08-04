# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSame(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, t1, t2):
        if not t1 and t2:
            print(t2.val)
            return False
        if not t2 and t1:
            print(t1.val)
            return False
        print("---------")
        if not t1 and not t2:
            return True
        if t1.val == t2.val:
            return self.isSame(t1.left, t2.left) and self.isSame(t1.right, t2.right)
        else:
            return False