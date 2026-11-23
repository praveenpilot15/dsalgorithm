import math
class Solution(object):
    def judgeSquareSum(self, c):
        a = 0  # starting with minimum possible square that is 0
        b = int(math.sqrt(c))  # maximum possible square number less than c to start checking,it is ub 
        while (a <= b):
            sumsq = a**2 + b**2
            if sumsq == c:
                return True
            elif sumsq < c:
                a = a + 1  # value is small so increment a
            else:
                b = b - 1  # value is large so decrement b
        return False
