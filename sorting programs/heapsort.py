def heapsort(arr,size):
    for i in range(size//2,-1,-1):
        maxheap(arr,i,size)
    for j in range(size-1,-1,-1):
        t=arr[0]
        arr[0]=arr[j]
        arr[j]=t
        maxheap(arr,0,j)
        
def maxheap(arr,i,size):
    while (2*i+1<size):
        child=2*i+1
        if (arr[child+1]>arr[child] and child<(size-1)):
            child=child+1
        if (arr[child]>arr[i]):
            arr[child],arr[i]=arr[i],arr[child]
        i=child

data=[15,20,7,9,30]
print("befor sorting:",data)
heapsort(data,len(data))
print("\nafter sorting:",data)
            
