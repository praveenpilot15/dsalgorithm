# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        dummy=ListNode(0)
        dummy.next=head
        leftprenode=dummy
        leftcurrentnode=head
        if leftcurrentnode.next is None and left==right:
            return head
        for i in range(left-1):
            leftprenode=leftprenode.next
            leftcurrentnode=leftcurrentnode.next
        storeleftcurrent=leftcurrentnode
        prenode=None#new prenode to do reversing
        for i in range((right-left)+1):#formula to find where to stop like we stop in None position
            nextnode=leftcurrentnode.next 
            leftcurrentnode.next=prenode
            prenode=leftcurrentnode
            leftcurrentnode=nextnode
        leftprenode.next=prenode
        storeleftcurrent.next=leftcurrentnode 
        return dummy.next
