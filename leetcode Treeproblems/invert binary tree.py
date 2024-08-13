# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if root is None:
            return root
        def invert(root):
            if root is None:
                return
            leftnode=invert(root.left)
            rightnode=invert(root.right)
            #inverting
            root.left=rightnode
            root.right=leftnode
            return root
        a=invert(root)
        return a 
            
        
     
        
