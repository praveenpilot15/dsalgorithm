# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def checktree(n1, n2):
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None:
                return False
            if n1.val != n2.val:
                return False
            checkLR = checktree(n1.left, n2.right)
            checkRL = checktree(n1.right, n2.left)
            return checkLR and checkRL

        result=checktree(root.left, root.right)
        return result
