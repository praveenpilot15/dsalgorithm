# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        lb=1
        ub=n
        while (lb<=ub):
            mid=(lb+ub)//2
            if isBadVersion(mid):#inbuild leetcode function that returns True for bad vertion and False for good version
                ans=mid
                ub=mid-1
            else:
                lb=mid+1
        return ans
        
