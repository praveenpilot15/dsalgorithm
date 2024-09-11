# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def averageOfLevels(self, root):
        if root is None:
            return []
        queue=[root] 
        result=[]
        while len(queue)!=0:
            sz=len(queue)
            sum1=0
            for i in range(sz):
                node= queue.pop(0)
                sum1=sum1+node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(float(sum1) / sz)
        return result
