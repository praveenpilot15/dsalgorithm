class Solution(object):
    def searchInsert(self, nums, target):
        if not nums:
            return -1
        lb=0
        ub=len(nums)-1
        ans=len(nums)
        while (lb<=ub):
            mid=(lb+ub)//2
            if (nums[mid]>=target):
                ans=mid
                ub=mid-1
            else:
                lb=mid+1
        return ans
