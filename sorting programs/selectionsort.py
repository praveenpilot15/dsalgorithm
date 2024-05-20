def selectionsort(arr):
    size=len(arr)
    for i in range(0,size):
        minindex=i
        for j in range(minindex+1,size):
            if arr[j]<arr[minindex]:
                minindex=j
        a=arr[i]
        arr[i]=arr[minindex]
        arr[minindex]=a
    print(arr)
data=[5,3,2,4,1,10,6,7]
selectionsort(data)

