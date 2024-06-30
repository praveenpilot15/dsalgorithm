class Solution(object):
    def findKthLargest(nums, k):
        a=tuple(sorted(nums,reverse=True))
        return a[k-1]
    nums=[3,2,1,5,6,4]
    k=2
    print(findKthLargest(nums,k))
#arrenge in decending order and returmn k-1 th term for kth largest , arrange in ascending order and
#return k-1 term for kth smallest 
