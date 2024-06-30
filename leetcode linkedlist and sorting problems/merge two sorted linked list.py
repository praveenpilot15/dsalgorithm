# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head=ListNode()#creating temporary node first node is  head point first node
        temp=head#declaring temporary variable to hold head
        while list1 is not None and list2 is not None:
            if list1.val<list2.val:
                temp.next=list1
                list1=list1.next
            else:
                temp.next=list2
                list2=list2.next
            temp=temp.next
        if list1 is not None:#after sorting pushing if any element is present in the list1
            temp.next=list1
        else:#pushing balance list2 element
            temp.next=list2 
        return head.next  
