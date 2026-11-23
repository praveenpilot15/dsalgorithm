class Solution(object):
    def findKthPositive(self, arr, k):
        lb=0
        ub=len(arr)-1
        while (lb<=ub):
            mid=(lb+ub)//2
            missingcount=arr[mid]-(mid+1) #counta the missig elements form 1 to current value
            if missingcount<k:
                #then count is less we have to move right to get >=k
                lb=mid+1 #move right
            elif missingcount>=k:
                #we have got the value greater k then or equal to k
                ub=mid-1# now move left 
        ans=lb+k #lb value holds the value number of missing elements becomes at least k.
        #if 4 means there are 4 elements before the k
        return ans
#first we find the total missing count
#if missing count <k we need to move right to get further missing values that is >=k 
#then missingcount >= then we move left to end the loop
#finaly answer is lb + k means lb will have the count of elements before k if k is 5 then lb will have 4 so 9 is missing
