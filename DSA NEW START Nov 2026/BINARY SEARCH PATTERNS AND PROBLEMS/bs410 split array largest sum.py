class Solution(object):
    def splitArray(self, nums, k):
        if not nums:
            return -1
        lb=max(nums) #to split subarrays
        ub=sum(nums) #to find largest sum
        ans=ub
        while (lb<=ub):
            mid=(lb+ub)//2
            if self.cansplit(mid,nums,k):
                ans=mid
                ub=mid-1
            else:
                lb=mid+1
        return ans
    def cansplit(self,guesssum,nums,k):
        currentsplit=1
        currentsum=0
        for num in nums:
            if (currentsum+num)>guesssum:
                currentsplit+=1
                currentsum=num
            else:
                currentsum+=num
        return currentsplit<=k
        
