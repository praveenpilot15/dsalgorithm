# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        #idea is when the two pointers loop and at a certain position they
        #will point to the same value and we confirm its loop else not loop 
        if head is None:
            return False
        elif head.next is None:
            return False
        slowptr=head
        fastptr=head
        while slowptr is not None and fastptr is not None and fastptr.next is not None:
            slowptr=slowptr.next
            fastptr=fastptr.next.next
            if slowptr==fastptr:
                return True
        return False
     
