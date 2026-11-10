class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1 and not nums2:
            return -1
        merged=nums1+nums2
        merged.sort()
        n=len(merged)
        mid=n//2
        if n%2==0:
            median=(merged[mid-1]+merged[mid])/2.0 #divide by 2.0 to get float value as 2.5 
            return median
        else:
            return float(merged[mid])
        
