# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        diameter=[0]#to use the value globaly after changing so we assign as list
        def traverse(root,diameter):
            if root is None:
                return 0
            left=traverse(root.left,diameter)
            right=traverse(root.right,diameter)
            height=max(left,right)+1
            if (left+right)>diameter[0]:#to check whether left+rightis>diameter value
                diameter[0]=left+right#reassigning the value of index 0 of list
            return height
        traverse(root,diameter)
        return diameter[0]#returning lists first value which holds the diameter of tree
