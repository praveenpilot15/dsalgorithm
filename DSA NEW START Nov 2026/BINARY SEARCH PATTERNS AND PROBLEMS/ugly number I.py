class Solution(object):
    def isUgly(self, n):
        if n<=0:
            return False
        while n%2==0:
            n=n//2 
        while n%3==0:
            n=n//3
        while n%5==0:
            n=n//5
        return n==1
        
#as per the given condition a number should be divisible by prime factor 235 so finally if it is for example if it is of 30 it is 2 * 3 * 5 so if it is divisible we are checking using while look why we are using while loops it can be off her number like 40 which is can be divisible by 2 two times or three times like 40 means we can get 20 then 10 so we use while loop finally if the answer is one it is true because the prime factor is 235 so it is not ugly  return calls
        
