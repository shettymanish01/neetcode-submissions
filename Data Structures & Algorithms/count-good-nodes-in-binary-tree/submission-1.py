# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return None
        stack = [[root, root.val]]
        good_nodes = 0


        while stack:
            temp = []
            for node, val in stack:
                if node:
                    if node.val >= val:
                        good_nodes += 1
                    temp.append([node.left, max(node.val, val)])
                    temp.append([node.right, max(node.val, val)])
                stack = temp
        return good_nodes
