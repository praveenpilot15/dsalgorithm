# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp=ListNode(0)#creating temporary node for head
        temp.next=head#giving temprory node as head
        leftptr=temp
        rightptr=temp
        for i in range(n):
            rightptr=rightptr.next
        while rightptr.next is not None:
            leftptr=leftptr.next
            rightptr=rightptr.next
        leftptr.next=leftptr.next.next
        return temp.next
#we declear two pointer and delete the nth element from end  ,first we move right pointer to the nthposition from first and when
#right pointer is not none we move left pointer to next value and right pointer from nth of from first till thr right pointer is none
#now when the right pointer is the ;left pointer will be at previous node from removing node
#now we declear the address of next node s next node to delete the node in between like left.next=left.next.next
#as list is mutable all the changes will be reflected in original list so we return temp.next which has head which is the original list

        
