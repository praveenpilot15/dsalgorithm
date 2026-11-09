arr=[-5,-2,0,1,2,4,5,6,7,10]
key=6
lb=0
ub=len(arr)-1
s=0
def binarysearch(arr,key,lb,ub):
    if (lb>ub):
        return None
    else:
        mid=(lb+ub)//2
        if (arr[mid]==key):
            print("Found Key : ",key," at index : ",mid)
            return mid
        elif (key>arr[mid]):
            return binarysearch(arr,key,mid+1,ub)
        elif (key<arr[mid]):
            return binarysearch(arr,key,lb,mid-1)
        else:
            return None
value=binarysearch(arr,key,lb,ub)
if (value==None):
    print("Key ",key,"Not Found")
    

    
