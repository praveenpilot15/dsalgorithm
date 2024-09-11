# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        head=TreeNode(0)#creating tree with element 0
        temp=[head]#using as list [0]will be stored
        def inorder(root,temp):
            if root is None:
                return
            inorder(root.left,temp)
            temp[0].right=TreeNode(root.val)#temps rightnode
            temp[0].left=None
            temp[0]=temp[0].right#assigning temp as added right to insert next value to right
            inorder(root.right,temp)
        inorder(root,temp)
        return head.right#head points 0 so its right has tree values 

      
  
