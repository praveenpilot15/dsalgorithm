def mergesort(arr,lb,ub):
    if lb<ub:
        mid=(lb+ub)//2
        mergesort(arr,lb,mid)
        mergesort(arr,mid+1,ub)
        merge(arr,lb,mid,ub)
def merge(arr,lb,mid,ub):
    i=lb
    j=mid+1
    sorted=[]
    
    while (i<=mid and j<=ub):
        if arr[i]<arr[j]:
            sorted.append(arr[i])
            i=i+1
    
        else:  #arr[i]>arr[j]
            sorted.append(arr[j])
            j=j+1
        
    if i>mid:
        while j<=ub:
            sorted.append(arr[j])
            j=j+1
    
    elif j>ub:
        while i<=mid:
            sorted.append(arr[i])
            i=i+1
    for p in range(len(sorted)):
        arr[lb+p]=sorted[p]
data=[1,2,8,5,4,6,100,12,86,45,23,0,65,1,8,5,23]
print("befor sorting :",data)
mergesort(data,0,len(data)-1)
print("\nafter sorting :",data)