class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        n=len(citations)
        for i in range(len(citations)):
            h=n-i#to take total papers after kept index , to take h and check citations are >=h so atleast 1 paper has atleast 1 citations 
            if citations[i]>=h:
                return h
        return 0
        
#check  2 nd nots for solved testcase and explanation
