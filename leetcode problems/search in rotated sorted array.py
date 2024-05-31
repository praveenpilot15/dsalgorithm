#modified binary search
def search(nums,target):
    lb=0
    ub=len(nums)-1
    while lb<=ub:
        mid=(lb+ub)//2
        if nums[mid]==target:
            return mid
        elif nums[lb] <= nums[mid]:
            if nums[lb]<= target <= nums[mid]:
                ub=mid-1
            else:
                lb=mid+1
        else:
            if nums[mid]<target <=nums[ub]:
                lb=mid+1
            else:
                ub=mid-1
    return -1
nums=[5,1,3]
target=5
print(search(nums,target))

#for understading workout with an example 
