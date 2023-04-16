class Solution:
    def climbStairs(self, n: int) -> int:
        
        if(n<=2):
            return n

        stepsNums = [0]*(n+1)

        stepsNums[1] = 1
        stepsNums[2] = 2
         
        for i in range(3, n+1):
            stepsNums[i] = stepsNums[i-1]+stepsNums[i-2]

        return stepsNums[n]