# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        if head.next is None:#if there is only one element
            return True
        def reverselist(current):#to reverse secound part of list and check with first part to check wether they are same if same true palindrome 
            prenode=None
            while current is not None:
                nextnode=current.next
                current.next=prenode
                prenode=current
                current=nextnode

            return prenode#prenode is head of reversed list
        ptr1=head
        ptr2=head
        while ptr1 is not None and ptr1.next is not None:#to find the middle of list
            ptr1=ptr1.next.next
            ptr2=ptr2.next#when ptr1 is none then ptr2 points the middle element
        if ptr1 is not None:#for the list with size of odd number
            ptr2=ptr2.next
        ptr2=reverselist(ptr2)#functiomn call
        ptr1=head
        while ptr2 is not None:
            if ptr1.val!=ptr2.val:#if ptr1 and ptr2 of reversed list are not same then not palindrome
                return False#return false
            ptr1=ptr1.next
            ptr2=ptr2.next
        return True#if no condition is satisfied in loop then its palidrome so its true
