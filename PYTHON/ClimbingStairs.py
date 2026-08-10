class Solution(object):
    def climbStairs(self, n):

        if n <= 2 :
            return n
        
        step1 = 1
        step2 = 2
        for i in range(3, n+1):

            curr = step1+step2

            step1 = step2
            step2 = curr

        return step2
