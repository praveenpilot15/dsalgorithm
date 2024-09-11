# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        def postorder(root):
            if root.left is None and root.right is None:
                if root.val==0:#0 means False
                    return False
                if root.val==1:#1 means True
                    return True
            #postorder is left->right->root
            left=postorder(root.left)
            right=postorder(root.right)
            if root.val==2:#2 means or operator
                return left or right
            if root.val==3:#3 means and operator
                return left and right
        return postorder(root)
        
