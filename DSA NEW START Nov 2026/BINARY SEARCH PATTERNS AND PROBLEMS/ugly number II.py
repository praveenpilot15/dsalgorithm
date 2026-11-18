#we have to find the list of ugly number till n and return the nth ugly number last number
#so as given ugly number meanse any number divisible by the combination of 2,3,5 for eg 30 ->2x3x5 's prime factor
#prime number means the number divisable by 1 and itselfd only
#to find solution multiply by 1 then any number multiplied with ugly number is ugly number only
class Solution(object):
    def nthUglyNumber(self, n):
        ugly=[1]#intially 1 to muliply with 2,3,5
        i2=i3=i5=0
        while (len(ugly)<n):
            a=ugly[i2]*2
            b=ugly[i3]*3
            c=ugly[i5]*5
            ugly_sort=min(a,b,c)#to put in list in ascending order so we can take the mth ugly number
            ugly.append(ugly_sort)
            if ugly_sort==a:
                i2+=1#to take next index and mulitiply with i2 as we have added it list
            if ugly_sort==b:
                i3+=1
            if ugly_sort==c:
                i5+=1
        return ugly[-1]#last value of list nth value

        
