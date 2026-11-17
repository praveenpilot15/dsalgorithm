class Solution(object):
    def mySqrt(self, x):
        lb=0
        ub=x
        res=0
        while lb<=ub:
            mid=(lb+ub)//2
            if mid*mid > x:#if mid**2 value we check if greater check left side for reducing value to get its root
                ub=mid-1
            elif mid*mid < x:
                lb=mid+1
                res=mid
            else:
                return mid
        return res
