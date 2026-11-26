class Solution(object):
    def findMinimumTime(self, tasks):
        tasks.sort(key=lambda x:x[1])
        #sorting  b ased on end value the above line will perform internal looping and get x[1] that end value in each neasted list beacuse (ascending ord er) for greedy approch 
        #we do this bcz selecting on time on 1 st task by greedy approch may helpfull in resuing it in next task if its in that range as we have arranged in acending order 
        #eg [1,3,2]->selected 2,3 now in [2,5,3] we can reuse 2,3 thats y sorting with end in ascending order 
        #as per greedy approch we always select from righmost and and move left
        run=[False]*2001 #2001 values can be given as per questions constraint
        total=0#to track number of run is on or True
        for start,end,duration in tasks:
            count=0#for each task we have to count how much are ruining thats is true , run count will calculated
            for t in range(start,end+1):
                if run[t]:
                    count+=1#if any run is true then count as we are counting already on count
            remaining=duration-count #Still how much we need to on so duration-count gives if we have 2 aleady on but 3 rd tasks need 3 then we need 3-2 = 1 , 1 is needed
            g=end #as per greedy approch we select from rightmost to left
            while (remaining>0):#if we need to on aditional system
                if not run[g]:#if not on thats is false 
                    run[g]=True#turning it on make True
                    total+=1#total system on we increment due to 1 onned now
                    remaining-=1#one onned so remaining decreses 
                g-=1#To select next leftvalue from end ,taking backward as pr greedy approch , if ,if statement not statisfied that is if it is already true or on then we have to go to next left value to check even even if we make it on then also g-=1 to check next left value
        return total #finally has the total system ON



        
