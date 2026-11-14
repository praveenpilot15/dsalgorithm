class Solution(object):
    def fixedPoint(self, arr):
        lb=0
        ub=len(arr)-1
        ans=-1 
        while (lb<=ub):
            mid=(lb+ub)//2
            if arr[mid]==mid:
                ans=arr[mid]
                ub=mid-1#to check first occurence match value to index
            elif mid<arr[mid]:
                ub=mid-1 #check left for match
            else:#if index is greater check right side for match
                lb=mid+1
        if ans==-1:
            return -1
        else:
            return ans
