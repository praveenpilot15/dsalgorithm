class Solution(object):
    def getCommon(self, nums1, nums2):
        if not nums1 and not nums2:
            return -1
        result_set=set()
        for num in nums1:
            if (self.is_there(num,nums2)):
                result_set.add(num)
        result_list=list(result_set)
        if result_list:#if element in list 
            return min(result_list)
        else: #if empty no match return -1
            return -1
    def is_there(self,num,nums2):
        lb=0
        ub=len(nums2)-1
        while (lb<=ub):
            mid=(lb+ub)//2
            if nums2[mid]==num:
                return True
            elif num>nums2[mid]:
                lb=mid+1
            else:
                ub=mid-1
        return False
        
