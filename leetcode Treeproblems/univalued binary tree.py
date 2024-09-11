# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        lst=[]
        def preorder(root,lst):
            if root is None:
                return
            lst.append(root.val)
            preorder(root.left,lst)
            preorder(root.right,lst)
        preorder(root,lst)
        c=0
        for i in range(len(lst)):
            if lst.count(lst[i])>c:
                c=lst.count(lst[i])
        if c==len(lst):
            return True
        return False
    
