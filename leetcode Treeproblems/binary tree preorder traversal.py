# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        if root is None:
            return root
        result=[]
        def preorder(root,result):
            if root is None:
                return
            result.append(root.val)
            preorder(root.left,result)
            preorder(root.right,result)
            return result
        a=preorder(root,result)
        return a
