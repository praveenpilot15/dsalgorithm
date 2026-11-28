class Solution(object):
    def maximumCount(self, nums):
        lb=0
        ub=len(nums)-1
        negative=0
        while (lb<=ub):
            mid=(lb+ub)//2
            if (nums[mid]<0):
                negative=mid+1#if mid is 2 and value is -1 then we have 3 negative numbers like 0,1,2 so mid + 1 gives answer 2+1=3
                lb=mid+1#to check further right for any negative numbers are there 
            else:
                ub=mid-1#moving left to check and it's an end case for while 

        lb=0
        ub=len(nums)-1
        positive=0
        while (lb<=ub):
            mid=(lb+ub)//2
            if (nums[mid]>0):
                positive=len(nums)-mid#if mid is an postive number then after mid all numbers are positive so we subract lenghth-mid we get total positive number 
                ub=mid-1#to check further left for any positive numbers 
            else:
                lb=mid+1# if we get mid like 0 we move right to check for any positive numbers 

        return max(positive, negative)
