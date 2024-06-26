# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object): 
    def getDecimalValue(self, head):
        def length(head):
            count=0
            while head is not None:
                count=count+1
                head=head.next
            return count
        size=length(head)
        addval=0
        i=0
        while i<=size and head is not None:
            size-=1
            bval=(2**size)*head.val
            addval=addval+bval
            head=head.next
        return addval
