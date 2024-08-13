# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0
        def calltree(root, sumleft,check):
            if root is None:
                return sumleft
            if root.left is None and root.right is None and check:
                sumleft =sumleft+root.val
            if root.left is not None:
                sumleft = calltree(root.left, sumleft, True)
                #TRue we pass to check whether it is left node
            if root.right is not None:
                sumleft = calltree(root.right, sumleft, False)
                #we need only left so we give false for right
            return sumleft
        return calltree(root, 0, False)#for root we pass false we need only
            
            
            
           
            
       
        
