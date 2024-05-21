def part(arr,lb,ub):
    pi=arr[lb]
    start=lb
    end=ub
    while (start<end):
        while start<end and   arr[start]<=pi:
            start=start+1
        while (end>=start and arr[end]>pi):
            end=end-1
           
        if (start<end):
            
            arr[start],arr[end]=arr[end],arr[start]
            
    arr[lb],arr[end]=arr[end],arr[lb]
    
    return end
def quick(arr,lb,ub):
    if lb<ub:
        loc=part(arr,lb,ub)
        
        quick(arr,loc+1,ub)
      
        quick(arr,lb,loc-1)
    
    

    
    
a=[7,6,10,5,9,2,1,15,7]
b=tuple(a)
print("before sorting  :",list(b))
size=len(a)
quick(a,0,size-1)
print("\nafter sorting :",a)
