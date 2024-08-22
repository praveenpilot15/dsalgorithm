# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        stk=[]
        def preorder(root,stk):
            if root is None:
                return
            if root.val not in stk:
                stk.append(root.val)
            preorder(root.left,stk)
            preorder(root.right,stk)
        preorder(root,stk)
        stk.sort()
        if len(stk)>1:
            return stk[1]
        else:
            return -1
