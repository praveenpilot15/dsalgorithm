class Solution(object):
    def kWeakestRows(self, mat, k):
        arr=[]
        for i in range(len(mat)):
          soldiersum=sum(mat[i])#count of soldiers in each row 
          arr.append((soldiersum,i))
             #appending tuple of soldiersum and index
        arr.sort()#sorting week to strong 
        result=[]
        for j in range(k):
            result.append(arr[j][1])
            #appending index
        return result
        
