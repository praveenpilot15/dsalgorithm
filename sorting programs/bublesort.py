


def bublesort(arr):
    size=len(arr)
    for i in range(0,size-1):
        for j in range(0,size-i-2):
            if arr[j]>arr[j+1]:
                a=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=a
    print(arr)
data=[5,3,2,4,1,10,6,7]
bublesort(data)
