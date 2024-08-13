# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        if root is None:
            return root
        result=[]
        def postorder(root,result):
            if root is None:
                return 
            postorder(root.left,result)
            postorder(root.right,result)
            result.append(root.val)
            return result
        a=postorder(root,result)
        return a
     
