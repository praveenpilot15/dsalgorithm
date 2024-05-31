
class Solution(object):
    def sortColors(nums):
        for i in range(0,len(nums)):
            minindex=i
            for j in range(minindex+1,len(nums)):
                if nums[j]<nums[minindex]:
                    minindex=j
            c=nums[i]
            nums[i]=nums[minindex]
            nums[minindex]=c
        return nums
    nums=[0,8,1,1,2,3,4]
    print('''Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort funct\n''')
    print(sortColors(nums))
