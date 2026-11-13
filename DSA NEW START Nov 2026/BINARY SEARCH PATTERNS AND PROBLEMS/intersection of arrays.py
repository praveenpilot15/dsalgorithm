class Solution(object): #intersection means common elements in two arrays need without duplicate
    def intersection(self, nums1, nums2):
        if not nums1 and not nums2:
            return -1
        nums2.sort()
        result_set=set() #set acctually by defult eliminates duplicate
        for num in nums1:
            if (self.is_bfs(nums2,num)):
                result_set.add(num)
        return list(result_set)
    def is_bfs(self,num2,num):
        lb=0
        ub=len(num2)-1
        while (lb<=ub):
            mid=(lb+ub)//2
            if num2[mid]==num:
                return True
            if num>num2[mid]:
                lb=mid+1
            else:
                ub=mid-1
        return False
        
