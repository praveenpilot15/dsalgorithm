class Solution(object):
    def shipWithinDays(self, weights, days):
        if not weights:
            return -1
        mincapacity=max(weights)#lb value refer notes max value to ship all weights
        maxcapacity=0
        for i in weights:
            maxcapacity+=i
        while (mincapacity<=maxcapacity):
            mid=(mincapacity+maxcapacity)//2
            days1=1 #let 1st day be mid kgs package shipping mid=10 10kgs shiping 
            sum1=0
            for i in weights:
                if (sum1+i)>mid:
                    days1+=1
                    sum1=0 #base condition to check next greater value
                sum1+=i
            if (days1>days):
                mincapacity=mid+1
            else:
                maxcapacity=mid-1
        return mincapacity
        
