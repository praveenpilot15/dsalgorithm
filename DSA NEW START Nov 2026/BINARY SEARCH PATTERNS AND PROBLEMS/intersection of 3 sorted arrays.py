class Solution(object):#to find common value in 3 arrays without duplicat
    def arraysIntersection(self, arr1, arr2, arr3):
        if not arr1 or not arr2 or not arr3:
            return []
        arr1arr2=set()
        for num in arr1:
            if self.is_bfs(arr2,num):
                arr1arr2.add(num)
        final1=list(arr1arr2) #compared arr1 and arr2 and found common elements
        finalarr3=set() #comparing arr1arr2 common elements with arr3
        for num in final1:
            if self.is_bfs(arr3,num):
                finalarr3.add(num)
        final=list(finalarr3)
        final.sort()  #the set does not give in sorted order so added sort () to sort it     
        return final
    def is_bfs(self,arr,num):
        lb=0
        ub=len(arr)-1
        while (lb<=ub):
            mid=(lb+ub)//2
            if (arr[mid]==num):
                return True
            elif num>arr[mid]:
                lb=mid+1
            else:
                ub=mid-1
        return False

        
