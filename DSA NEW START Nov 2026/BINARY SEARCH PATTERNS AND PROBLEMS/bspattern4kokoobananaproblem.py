#pattern 4 :binary search on anser Monkey banana problem
import math
piles=[3,6,7,11]
h=8
def minimumspeed(piles,h):
    lb=1
    ub=max(piles)
    ans=ub
    while (lb<=ub):
        mid=(lb+ub)//2
        if is_possible(piles,mid,h): #template
            ans=mid
            ub=mid-1
        else:
            lb=mid+1
    return ans
def is_possible(piles,mid,h): #helper function
    time=0
    for i in piles:
        time+=(i+(mid-1))//mid #ceil function not working in leetcode
    if (time<=h):
        return True
    else:
        return False
minspeed=minimumspeed(piles,h)
print("Minimum speed to eat is : ",minspeed)

    
