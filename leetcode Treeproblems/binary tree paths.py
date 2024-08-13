# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        if root is None:
            return []
        result = []
        def path(node, currentpath,result):
            if node is not None:
                currentpath += str(node.val)
                if node.left is None and node.right is None:
                    result.append(currentpath)
                    return
                else:
                    currentpath += "->"
                    path(node.left, currentpath,result)
                    path(node.right, currentpath,result)
        
        path(root, "",result)
        return result
