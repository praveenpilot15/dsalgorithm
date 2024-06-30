# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if head is None:
            return None
        elif head.next is None:
            return None
        slowptr=head
        fastptr=head
        while fastptr is not None and fastptr.next is not None:
            fastptr=fastptr.next.next
            slowptr=slowptr.next
            if (fastptr==slowptr):
                fastptr=head
                while (fastptr!=slowptr):
                    fastptr=fastptr.next
                    slowptr=slowptr.next
                return fastptr
        return None
