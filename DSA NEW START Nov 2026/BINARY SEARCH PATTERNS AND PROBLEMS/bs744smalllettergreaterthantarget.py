class Solution(object):
    def nextGreatestLetter(self, letters, target):
        lb=0
        ub=len(letters)-1
        ans=letters[0]
        while (lb<=ub):
            mid=(lb+ub)//2
            if (letters[mid]>target):
                ans=letters[mid]
                ub=mid-1
            else:
                lb=mid+1
        return ans

