# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dl1=l1
        dl2=l2
        list1=[]
        list2=[]
        while dl1 is not None or dl2 is not None:
            if dl1 is not None:
                list1.append(str(dl1.val))
                dl1=dl1.next
            if dl2 is not None:
                list2.append(str(dl2.val))
                dl2=dl2.next
        list1.reverse()
        list2.reverse()

        integerval=int(''.join(list1))
        integerval2=int(''.join(list2))

        sumval=integerval+integerval2
        stringval=str(sumval)

        head=ListNode(stringval[-1])
        temp=head
        for i in stringval[-2::-1]:
            temp.next=ListNode(i)
            temp=temp.next
        return head


       
        
