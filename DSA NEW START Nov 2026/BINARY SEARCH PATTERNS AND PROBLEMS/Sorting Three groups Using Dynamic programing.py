class Solution(object):
    def minimumOperations(self, nums):
        dp1=0#minimum  changes if changing with 1
        dp2=0#minimum changes if changing with 2
        dp3=0#minimum changes if changing with 3
        for x in nums:
            #Taking each element and checking the changes of 1,2,3 with constrient of non decresing order
            new_dp1=dp1+(x!=1) #make current element 1 and count changes 
            new_dp2=min(dp1,dp2)+(x!=2)#make current element 2 by taking the previous minimum change and count changes
            new_dp3=min(dp1,dp2,dp3)+(x!=3)#make current element 3 by taking the minimum of previous elemnets changes and count changes
            #Updating the Changes So next element can be decidede to Changed  or Leave it as if, if its in non decresing order
            dp1=new_dp1
            dp2=new_dp2
            dp3=new_dp3
        return min(dp1,dp2,dp3) #At end of all the elements in list we can get the changes required to make it in non decreasing order and we return the minimum changes required for the array to be in non decresing order

        
        
