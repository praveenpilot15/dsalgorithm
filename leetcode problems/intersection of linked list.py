# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        def length(head):
            count=0
            while head is not None:
                count+=1
                head=head.next
            return count
        sizeA=length(headA)
        sizeB=length(headB)
        while sizeA>sizeB:
            #to move the headA to the same pointing position of headB
            sizeA-=1
            headA=headA.next
        while sizeB>sizeA:
            #to move the headB to the same pointing position of headA
            sizeB-=1
            headB=headB.next
        #now both heads will be at same position in two list as we moved 
        while headA!=headB:
            #now to check headaA is not equal to headb and move them
            headA=headA.next
            headB=headB.next
        return headA 
