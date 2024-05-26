def linearsearch(arr,x):
    s=0
    for i in range(0,len(arr)):
        if arr[i]==x:
            s=1
            print("element found @ index ",i," value",arr[i])
            
        
    return s
a=[1,5,6,7,8]
x=7
b=linearsearch(a,x)
if b==0:
    print("element not found in list")
   
