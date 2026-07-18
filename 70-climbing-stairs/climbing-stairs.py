#
class Solution(object):
    
    def climbStairs(self, n):
      self.dp=[-1]*(n+1)
      
      def fun(n,dp):
        self.dp[0]=1
        self.dp[1]=1
        for i in range (2,n+1):
          dp[i ]= dp[i-1]+dp[i-2]
        return self.dp[n]
      return fun(n,self.dp)