arr=[1,2,4,4,4,4,4,4,6]
key=11
def firstoccur(arr,key):
    lb=0
    ub=len(arr)-1
    ans=-1
    while (lb<=ub):
        mid=(lb+ub)//2
        if (arr[mid]==key):
            ans=mid
            ub=mid-1
        elif (key>arr[mid]):
            lb=mid+1
        else:
            ub=mid-1
    return ans
def lastoccur(arr,key):
    lb=0
    ub=len(arr)-1
    ans=-1
    while (lb<=ub):
        mid=(lb+ub)//2
        if (arr[mid]==key):
            ans=mid
            lb=mid+1
        elif key>arr[mid]:
            lb=mid+1
        else:
            ub=mid-1
    return ans
value=firstoccur(arr,key)
value1=lastoccur(arr,key)
if (value==-1):
    print("Value not found")
else:
    print("First Occurence ia at : ",value)
if (value1==-1):
    print("Value not Found")
else:
    print("Last Occurence : ",value1)
