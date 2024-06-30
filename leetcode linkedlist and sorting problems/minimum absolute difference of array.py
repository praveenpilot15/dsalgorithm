def minimumabsoluteDifference(arr):
        arr.sort() #first we sort to check difference of consecutive values 
        diff=float('inf') #to set minimum abs difference as infinity first and we change as per condition
        res=[]
        for i in range(0,len(arr)-1):
            diff1=arr[i+1]-arr[i] #storing each differens
            if diff1<diff: #checking whether difference is less than minimum abs diff 
                diff=diff1 #change minimum abs diff as new diff when diff<minmum diff
                
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==diff: #check whick values difference is equal to minimum abs diff found above
                res.append([arr[i],arr[i+1]]) #push as nested list

        print("\nMinimumabsoluteDifferens value: ",diff)
        print("\nThe array values difference which satisfy the  minimumabsdiff  is: ",res)
data=[40,11,26,27,-20]
print('''QUESTION: Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

    *a, b are from arr
    *a < b
    *b - a equals to the minimum absolute difference of any two elements in arr''')
minimumabsoluteDifference(data)
