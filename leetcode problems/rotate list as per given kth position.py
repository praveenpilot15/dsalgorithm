# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head is None or k==0:
            return head
        
        temp=head
        loops=0
       
        while temp.next is not None:
            temp=temp.next
            loops+=1
        temp.next=head
        k=k%(loops+1)#keep the array in size not to exceed the size of list
        jump=(loops)-k
        temp=head
        for i in range(jump):
            temp=temp.next
        newhead=temp.next

        temp.next=None
        return newhead
