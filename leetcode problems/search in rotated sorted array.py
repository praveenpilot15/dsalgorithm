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
print('''There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.\n''')

print(search(nums,target))

#for understading workout with an example 
