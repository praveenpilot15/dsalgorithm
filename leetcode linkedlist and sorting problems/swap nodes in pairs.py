# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        headpoint=ListNode(0)#creating temporary node 
        headpoint.next=head
        ptr=headpoint#temporary pointer
        while ptr.next is not None and ptr.next.next is not None:
            firstnode=ptr.next#first element
            secondnode=ptr.next.next#second element

            firstnode.next=secondnode.next
            secondnode.next=firstnode

            ptr.next=secondnode#after swaping second mode will be first so change pointer to second 
            ptr=firstnode#change pointer to swaped first node so now new first node will be ptr.next which is next element 
        return headpoint.next
        
