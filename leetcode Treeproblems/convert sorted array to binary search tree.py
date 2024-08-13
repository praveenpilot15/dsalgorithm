# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        if nums is None:
            return None
        def binarysearchtree(nums,low,heigh):
            #same consept of binary search
            '''formula of binary seach
               low=mid+1
               heigh=mid-1
            '''
            if low>heigh:
                return None
            mid=(low+heigh)//2
            root=TreeNode(nums[mid])#creating a binary search tree
            root.left=binarysearchtree(nums,low,mid-1)
            root.right=binarysearchtree(nums,mid+1,heigh)
            return root
        return binarysearchtree(nums,0,len(nums)-1)
