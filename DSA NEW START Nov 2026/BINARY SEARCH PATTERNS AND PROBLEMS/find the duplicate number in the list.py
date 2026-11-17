class Solution(object):
    def findDuplicate(self, nums):
        lb=min(nums)#checking range form lb value to ub value
        ub=max(nums)#to check if duplicate is there in max element also till end we check all values below max value also we check duplicate
        while (lb<=ub):
            mid=(lb+ub)//2
            count=0
            for i in nums:
                if i<=mid:
                    count+=1 
            if (count>mid):#if count is greater then mid then duplicate is in left side only as we have 1 or 2 element extra then mid 
                ub=mid-1
            else:#if less then we have to check right if there is another element we can find if count greaters the mid
                lb=mid+1
        return lb #final lb will hold the value of duplicate
