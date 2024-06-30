# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prenode=None
   
        currentnode=head
        
        while currentnode is not None:
            nextnode=currentnode.next
            currentnode.next=prenode
            prenode=currentnode
            currentnode=nextnode
           
        return prenode
        
    
        
