# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        stk1=[]
        stk2=[]
        def preorder(root,stack):
            if root is None:
                return
            if root.left is None and root.right is None:
                stack.append(root.val)
                return
            preorder(root.left,stack)
            preorder(root.right,stack)
        preorder(root1,stk1)
        preorder(root2,stk2)
        if stk1==stk2:
            return True
        else:
            return False
