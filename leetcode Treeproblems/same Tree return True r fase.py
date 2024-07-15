# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        left=self.isSameTree(p.left,q.left)#recursively calling left subtree
        right=self.isSameTree(p.right,q.right)#recursively calling right subtree

        return left and right
