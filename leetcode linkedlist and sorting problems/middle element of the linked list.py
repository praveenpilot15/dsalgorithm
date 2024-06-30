# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        if head.next is None:
            return head
        ptr1=head
        ptr2=head

        while ptr1 is not None and ptr1.next is not None:
            ptr1=ptr1.next.next
            ptr2=ptr2.next
       
        return ptr2
