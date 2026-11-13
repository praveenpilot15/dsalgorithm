class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
      ans=float("inf") #assigning some large value inf - infinity
      #land rides first and water ride second
      for i in range(len(landStartTime)):
        land_finish=landStartTime[i]+landDuration[i]
        for j in range(len(waterStartTime)):
            water_start=max(land_finish,waterStartTime[j])#what if time exceded and water game started so we take max time
            total_finish=water_start+waterDuration[j]
            ans=min(ans,total_finish)
        #water ride first and land ride second 
      for i in range(len(waterStartTime)):
        water_finish=waterStartTime[i]+waterDuration[i]
        for j in range(len(landStartTime)):
            land_start=max(water_finish,landStartTime[j])
            total_finish=land_start+landDuration[j]
            ans=min(ans,total_finish)
      return ans
    
