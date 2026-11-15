class Solution(object):
    def kthSmallestSubarraySum(self, nums, k):
        lb=min(nums)
        ub=sum(nums)
        while (lb<ub):
            mid=(lb+ub)//2 #mid is our maximum allowed subarray sum for the current binary search
            left=0 #left value of the subarry
            curr=0 #current sum of the sunarray
            count=0 #total number of valid subarrays
            for right in range(len(nums)):
                curr+=nums[right] #current sum
                while (curr>mid): #check current sum >mid value
                     #we only allow sum <=mid 
                     curr-=nums[left] #removing left most element to take next suubarray
                     left+=1#increment 1 because we no need now firt element if first is 0 its removed now we have to look from 1
                count+=right-left+1 #counts the number of valid subarray at the current right index like [2,1] [1] so count is 2
            if (count>=k): #we have enough subarrays answer could be mid or something smaller so we check on left siide so ub=mid
                ub=mid #not mid-1 becuase answer can be at mid also
            else:
                lb=mid+1 #if subarray count is too small check on right side get greateter count

        return lb
