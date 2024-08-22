# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        def check(r,s):
            if r is None and s is None:
                return True
            if r is  None  or s is None:
                return False
            if r.val!=s.val:
                return False
            return check(r.left,s.left) and check(r.right,s.right)
        def same(root):
            if root is None:
                return False
            if check(root,subRoot) is True:
                return True
            return same(root.left) or same(root.right)
        return same(root)
       
        
