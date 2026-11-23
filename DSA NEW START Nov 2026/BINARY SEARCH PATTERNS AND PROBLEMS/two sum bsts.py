# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binarysearch(self,arr,target):
        lb=0
        ub=len(arr)-1
        while (lb<=ub):
            mid=(lb+ub)//2
            if arr[mid]==target:
                return True
            elif target>arr[mid]:
                lb=mid+1
            else:
                ub=mid-1
        return False
    def inorder(self,root,res): #inorder traversal
        if root is None:
            return
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)
    def twoSumBSTs(self, root1, root2, target):
        list1=[]
        list2=[]
        self.inorder(root1,list1)
        self.inorder(root2,list2)
        for num in list1:
            required=target-num #finding the second numvber of sum like if target is 10-> 2+8=10 then were 2 is list 1 value 10-2=8 we find wether 8 present in list 2 just changing the equation to check sum present
            if (self.binarysearch(list2,required)):#check list 2 has value if there then target sum present
                return True
        return False

#Take the first number from list1.
#Subtract that number from the target to get the required second number.
#Search for that required number in list2 using binary search.
#If it exists, return True because their sum equals the target.
#If it doesn't exist, take the next number from list1 and repeat.
#If no pair is found after checking all numbers, return False.
