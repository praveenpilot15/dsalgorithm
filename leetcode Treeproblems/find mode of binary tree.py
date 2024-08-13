# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        if root is None:
            return root
        d={}
        def checkval(a):
            if a not in d:
                d[a]=1
            if a in d:
                d[a]+=1
        def preorder(root):
            if root is None:
                return
            checkval(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        result=[]  
        mode=max(d.values())
        for key,value in d.items():
            if value == mode:
                result.append(key)
        return result
        
       
        
