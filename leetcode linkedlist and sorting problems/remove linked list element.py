# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        dummy=ListNode(0)
        dummy.next=head
        prenode=dummy
        while prenode.next is not None:
            if prenode.next.val==val:
                prenode.next=prenode.next.next
            else:
                prenode=prenode.next
        return dummy.next
     
        
