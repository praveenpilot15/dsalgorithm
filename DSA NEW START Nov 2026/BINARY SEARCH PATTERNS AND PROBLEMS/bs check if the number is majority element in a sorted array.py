class Solution(object):
    def isMajorityElement(self, nums, target):
        #to find total count of target present in list 
        #find first occurence and last occurence index 
        #formula count=lastocurence-firstoccurence+1
        if len(nums)==1:
            return False
        firstoccurence=self.firstoccur(nums,target)
        lastoccurence=self.lastoccur(nums,target)
        count=(lastoccurence-firstoccurence)+1 #total count of target in nums list
        majoritycheck=len(nums)/2
        if count>majoritycheck:
            return True
        else:
            return False
    def firstoccur(self,nums,target):
        lb=0
        ub=len(nums)-1
        startindex=0
        while (lb<=ub):
            mid=(lb+ub)//2
            if nums[mid]==target:
                startindex=mid
                ub=mid-1
            else:
                lb=mid+1
        return startindex
    def lastoccur(self,nums,target):
        lb=0
        ub=len(nums)-1
        lastindex=0
        while (lb<=ub):
            mid=(lb+ub)//2
            if nums[mid]==target:
                lastindex=mid
                lb=mid+1
            else:
                ub=mid-1
        return lastindex
        
