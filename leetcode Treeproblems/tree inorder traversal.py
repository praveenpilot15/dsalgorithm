# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        #inorder- LEFT->ROOT->RIGHT
        if root is None:
            return root
        result=[]
        def inorder(node):
            if node is not None:
                inorder(node.left)#LEFT
                result.append(node.val)#ROOT
                inorder(node.right)#RIGHT
        inorder(root)
        return result
