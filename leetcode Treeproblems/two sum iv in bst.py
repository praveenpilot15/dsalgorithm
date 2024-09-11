# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        if root is None:
            return False
        lst=[]
        def preorder(root,lst):
            if root is None:
                return
            lst.append(root.val)
            preorder(root.left,lst)
            preorder(root.right,lst)
        preorder(root,lst)
        lst.sort()
        print(lst)
        left=0
        right=len(lst)-1
        while left<right:
            sum1=lst[left]+lst[right]
            if sum1==k:
                return True
            elif sum1>k:
                right=right-1
            else:#sum1<k
                left=left+1
        return False
