class Solution(object):
    def findMin(self, nums):
        if not nums:
            return -1
        lb=0
        ub=len(nums)-1
        while (lb<ub):
            mid=(lb+ub)//2
            if (nums[mid]>nums[ub]): #check right array so we need lb
                lb=mid+1
            else:#check left array so we need ub
                ub=mid #there can be minimum in mid also so ub = mid
        return nums[lb] #final lb index holds the minimum value
        
