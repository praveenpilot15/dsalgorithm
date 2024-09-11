# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        def traverse(root,sum):
            if root is None:
                return 0
            sum=2*sum+root.val
            if root.left is not None or root.right is not None:
                leftsum=traverse(root.left,sum)
                rightsum=traverse(root.right,sum)
                return leftsum+rightsum
            if root.left is None and root.right is None:
                return sum
        return traverse(root,sum=0)
        
