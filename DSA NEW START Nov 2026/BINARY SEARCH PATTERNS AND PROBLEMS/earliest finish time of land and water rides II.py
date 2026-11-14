class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        #optimised approch single longs to avoid Time lime extending error
        #GOING ON WITH LAND RIDE FIRST AND WATER RIDE SECOND
        min_land_finish=float("inf")
        for i in range(len(landStartTime)): #going for land ride first
            total_time=landStartTime[i]+landDuration[i]
            if total_time<min_land_finish:
                min_land_finish=total_time #minimum time to finish land ride
        #after land ride going to water ride
        best_finish_time=float("inf")
        for j in range(len(waterStartTime)):
            actualwaterstart=max(min_land_finish,waterStartTime[j])#we take maximum time to get the total finishtime of both rides
            total_time1=actualwaterstart+waterDuration[j]
            if total_time1<best_finish_time:
                best_finish_time=total_time1
        option1=best_finish_time #earliest time in land ride first water ride second
        #NOW GOING WITH WATER RIDE FIRST LAND RIDE SECOND
        min_water_finish=float("inf")
        for i in range(len(waterStartTime)):#water ride first
            total_time=waterStartTime[i]+waterDuration[i]
            if total_time<min_water_finish:
                min_water_finish=total_time
        #now to land ride
        best_finish_time=float("inf")
        for j in range(len(landStartTime)):
            actuallandstart=max(min_water_finish,landStartTime[j])
            total_time1=actuallandstart+landDuration[j]
            if (total_time1<best_finish_time):
                best_finish_time=total_time1
        option2=best_finish_time
        if option1<option2:
            return option1
        else:
            return option2
                
