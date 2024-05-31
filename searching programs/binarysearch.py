def binarysearch(arr,lb,ub,x):
    s=0
    if lb>ub:
        return None
    else:
        mid=(lb+ub)//2
        if arr[mid]==x:
            s=-1
            print("element found @ ",mid," value",arr[mid])
        elif x>arr[mid]:
            lb=mid+1
            return binarysearch(arr,lb,ub,x)
        elif x<arr[mid]:
            ub=mid-1
            return binarysearch(arr,lb,ub,x)
    return s
data=[0,1,2,4,5,6,7]
x=0
r=binarysearch(data,0,len(data)-1,x)
if (r==None):
    print("element not found in array")
