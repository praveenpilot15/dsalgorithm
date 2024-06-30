# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        temp=ListNode(0)
        temp.next=head
        previousnode=temp
        while head is not None and head.next is not None:
            if head.val == head.next.val:
                while head.next is not None and head.val==head.next.val:
                    head=head.next
                previousnode.next=head.next
            else:
                previousnode=previousnode.next
            head=head.next
                
            
        return temp.next
