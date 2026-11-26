 #increemble submarine count means we have to remove and submarine from the given number after removing also it should be a strictly increasing their it is called as an incredible submarine so we have to return the count of possible arrys that are strictly increasing [] is also considered as one possible strict increasing submarray
class Solution(object):
    def incremovableSubarrayCount(self, nums):
        n=len(nums)
        count=0 #to count increemovable submarray
        #implementing nested loop to take the reminding subarray after removal 
        for i in range(n):
            for j in range(i,n):
                remaining=nums[:i]+nums[j+1:] #values remain after removal of an subarray
                valid=True #first assuming it is strictly increasing 
                for k in range(1,len(remaining)):#to check it is strictly increasing 
                   if remaining[k]<=remaining[k-1]:
                     valid=False #if index 1 value is greater than index zero value then it is not strictly increasing so changing False
                     break 
                if valid:
                    count+=1
        return count
                    
            
                    
        
