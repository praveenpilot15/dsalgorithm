class Solution(object):
    def missingElement(self, nums, k):
        n=len(nums)
        total_missing=nums[-1]-nums[0]-(n-1) #formula to find total missing elements in an list nums
        if (k>total_missing):
            #if k value is > missing value then the value is present after last element
            #value present after the list like if list end with 10 then k th index value may be 12 \
            return nums[-1]+(k-total_missing) #last value + requiredindex value -total missing
            #[1,2,4] k=3  -> 4+ (3-1)->4+2->6 ans missing are [3,5,6] 3rd missing value is 6 
        #If not satisfied with above condition then missing value present inside list we use binary search
        lb=0
        ub=n-1
        while (lb<=ub):
            mid=(lb+ub)//2
            missing_count=nums[mid]-nums[0]-mid #formula to find total missing values before an index 
            if missing_count<k:#we need at k but its less we move right to take next index
                lb=mid+1
            else:
                ub=mid-1
        prev=lb-1 #to take m
        alreadymissing=nums[prev]-nums[0]-prev #To find missing numbers before the previous index
        remaining=k-alreadymissing #to get still how much we remaining if k=3 then alreadymissing=2 then still we need 1 to get 3 so 1 is remaining 
        return nums[prev]+remaining #finaly previous element + how much we need or remaining
    
        
        
