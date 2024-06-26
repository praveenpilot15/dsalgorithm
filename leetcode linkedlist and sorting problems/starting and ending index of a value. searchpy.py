def search(nums,target):
    def firstpos(nums,target):
        lb=0
        ub=len(nums)-1
        while lb<=ub:
            mid=(lb+ub)//2
            if target>nums[mid]:
                lb=mid+1
            else:
                ub=mid-1
        return lb
    def lastpos(num,target):
        lb=0
        ub=len(nums)-1
        while lb<=ub:
            mid=(lb+ub)//2
            if target>=nums[mid]:
                lb=mid+1
            else:
                ub=mid-1
        return ub
    startpos=firstpos(nums,target)
   
    endpos=lastpos(nums,target)
   
    if startpos<=endpos and nums[startpos]==target and startpos<len(nums):
        return [startpos,endpos]
    else:
        return [-1,-1]
nums=[5,7,7,8,8,10]
target=8
print('''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.\n''')
print(search(nums,target))
