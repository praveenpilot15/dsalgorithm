arr=[1,2,4,4,4,4,4,4,6]
key=4
def lowerbound(arr,key): #To find the insert position of the key in the sorted order
    lb=0
    ub=len(arr)-1
    ans=len(arr)#if target value is greater then the last value of arr then return next index to insert it
    #as it is greater than all the elements in array so it goes to las pos so we assign ans with len(arr)
    while (lb<=ub):
        mid=(lb+ub)//2
        if (arr[mid]>=key):
            ans=mid
            ub=mid-1#to validate left if any > value there than key
        elif (key>arr[mid]):
            lb=mid+1
    return ans
def upperbound(arr,key):#Fist greatest value then the key
    lb=0
    ub=len(arr)-1
    ans=len(arr)
    while (lb<=ub):
        mid=(lb+ub)//2
        if (arr[mid]>key):
            ans=mid
            ub=mid-1
        else:
            lb=mid+1
    return ans
value=lowerbound(arr,key)
if (value!=len(arr)):
    print("Key can be inserted at the index : ",value)
else:
    print("key can be inserted at ",len(arr))
value1=upperbound(arr,key)
if value1==len(arr):
    print("The Greatest not in array")
else:
    print("The Fist greater Value then key ",key,"is : ",arr[value1])



            
    
