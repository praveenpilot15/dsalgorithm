#132 pattern means the left element should be lower middle should be grater and last elemet should be less then middle which should statisfy the condition 1<2<3 which we call it as 132 pattern if exits we return true else false
class Solution(object):
    def find132pattern(self, nums):
        stack=[] #stores the largest possible element like 3 in 132 pattern
        two=float("-inf")#-infinity means lowest value then any number and TWO STORES THE RIGHT MOST VALUE LIKE 2 IN 132 PATTERN OR MIDDLE ELEMENT IN 1<2<3
        for num in reversed(nums): #revert the list to check from right to left [3,2,1]
            if num<two:#finds the left most value that is 1 in 132 patterm
                return True #if statisfied then 132 paqttern present so true
            while stack and num>stack[-1]:#check the left most value that like 2 in 132 pattern
                two=stack.pop()#pop in stack store in two
            stack.append(num)#append num as found greater and check in next loop
        return False

        
        
