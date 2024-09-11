# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        lst=[]
        def preorder(root):
            if root is None:
                return
            lst.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        sum1=0
        for i in lst:
            if i>=low and i<=high:
                sum1=sum1+i
        return sum1
