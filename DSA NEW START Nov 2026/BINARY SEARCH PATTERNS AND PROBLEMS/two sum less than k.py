class Solution(object):
    def twoSumLessThanK(self, nums, k):
        nums.sort()
        lb=0
        ub=len(nums)-1
        ans=-1
        while lb<ub:
            sum1=nums[lb]+nums[ub] #adding first value and last value
            if sum1<k: #if sum <k then we go for next index so lb+=1
                ans=max(ans,sum1)
                lb=lb+1
            else: #if sum if > then adding next lb index also will be > so ub-=1 taking next ub
                ub=ub-1
        if ans==-1:
            return -1
        else:
            return ans
            
        
