#pattern 5 :Rotated Sorted array
arr=[4, 5, 6, 7, 0, 1, 2]
key=0
def rotededarr(arr,key):
    lb=0
    ub=len(arr)-1
    while (lb<=ub):
        mid=(lb+ub)//2
        if arr[mid]==key:
            return mid
        if arr[lb]<=arr[mid]:#Template to find left array is sorted
            if (arr[lb]<=key<=arr[mid]):#template to find target present in left array
                ub=mid-1
            else:
                lb=mid+1
        else:
            if (arr[mid]<=key<=arr[ub]):#templete to find target present in right array
                lb=mid+1
            else:
                ub=mid-1
    return -1
value=rotededarr(arr,key)
if (value==-1):
    print("Value not Found")
else:
    print(key," present at index :",value)
