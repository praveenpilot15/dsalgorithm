# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        #minimum depth means the level at which first leaf node starts is called minimum depth 
        if (root is None):
            return 0
        mindepth=0
        queue=[root]
        while (len(queue)!=0):
            mindepth=mindepth+1
            s=len(queue)
            for i in range(s):
                node=queue.pop(0)
                if node.left is None and node.right is None:
                    return mindepth#minimum depth first leaf node
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return mindepth

