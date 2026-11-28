class Solution(object):
    def findBestValue(self, arr, target):
        lb=0#minimum value to choose
        ub=max(arr)#maximum value we can choose
        while (lb<=ub):
            mid=(lb+ub)//2
            total=0
            for i in arr:
                total+=min(i,mid)#if value in arr is graeter than choosen value then we replace with choosen value so here we sum chosen value only as 4,9 are greater
            if total>target:
                ub=mid-1 #as total exceeds the target
            else:
                lb=mid+1
        #finally after binary search we get a value like lb and ub which is the boundary were target lies between their sum like 9,11 target les b/w them lb=4 and ub=3 
        #Now we have check which value is close to target and if both have same difference then return small value
        totallb=0
        totalub=0 
        for i in arr:
            totallb+=min(i,lb)
            totalub+=min(i,ub)
        if abs(totallb-target)<abs(totalub-target):#abs means absolute value if abs(-5)->5 remove negative
            return lb
        else:
            return ub

# We are given an array and a target.
# We choose an integer value from 0 to the maximum element in the array.
# If an element is greater than our chosen value, we replace it with that value.
# If an element is less than or equal to our chosen value, it remains unchanged.
# We calculate the sum of this mutated array.
# We compare that sum with the given target.
# We find the chosen value that produces a sum closest to the target.
# If two chosen values produce sums equally close to the target, we return the smaller chosen value.
