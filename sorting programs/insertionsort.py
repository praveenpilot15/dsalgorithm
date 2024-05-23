def insertionsort(arr):
    size=len(arr)
    for i in range(0,size-1):
        for j in range(0,size-i-1):
            if arr[j]>arr[j+1]:
                b=j+1
                a=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=a
                for k in range(b,0,-1):
                    if arr[k]<arr[k-1]:
                        c=arr[k]
                        arr[k]=arr[k-1]
                        arr[k-1]=c
    print(arr)
data=[5,3,2,4,1,10,6,7,0,3,5,1,6,0,2,4,6]
insertionsort(data)
