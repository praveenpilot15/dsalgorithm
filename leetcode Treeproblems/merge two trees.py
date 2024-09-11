# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        if root1 is None and root2 is None:
            return root1
        def merge(r1,r2):
            if r1 is None:
                return r2
            if r2 is None:
                return r1
            r1.val=r1.val+r2.val
            r1.left=merge(r1.left,r2.left)
            r1.right=merge(r1.right,r2.right)
            return r1
        merged=merge(root1,root2)
        return merged
     
