#pattern 6 Binary search matrix (BSM):
matrix= [
  [1,  3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
]
key=30
def bsm(matrix,key):
    if not matrix or not matrix[0]: #if list is empty its false so not to true ,and if inside list is empty again false
        return -1 #to avoid empty lists or matrix
    lb=0
    ub=(len(matrix)*len(matrix[0])-1)#row*column=total count of values
    totalcolumn=len(matrix[0])
    while (lb<=ub):
        mid=(lb+ub)//2   #1D mid
        rowindex=mid//totalcolumn #1D->2D index Formula for BSM row index
        colindex=mid%totalcolumn #1D-> 2D index Formula for BSM column index
        if matrix[rowindex][colindex]==key:
             return [rowindex,colindex]
        if key>matrix[rowindex][colindex]:
            lb=mid+1
        else:
            ub=mid-1
    return -1
value=bsm(matrix,key)
if value==-1:
    print("Value Not Found")
else:
    print(key," Present at 2D index : ","matrix[",value[0],",",value[1],"]")
        
        
