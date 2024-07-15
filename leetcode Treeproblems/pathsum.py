# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        #path sum means addition of values from root to leaf mode if its equal to target than TRUE ELSE FALSE
        if root is None:
            return 0
        nodestack=[root]
        nodesum=[root.val]
        while (len(nodestack)!=0):
            node=nodestack.pop()
            pathsum=nodesum.pop()
            if ((node.left is None and node.right is None )and pathsum==targetSum):
                return True
            if node.left is not None:
                nodestack.append(node.left)
                nodesum.append(node.left.val+pathsum)
            if node.right is not None:
                nodestack.append(node.right)
                nodesum.append(node.right.val+pathsum)
        return False
