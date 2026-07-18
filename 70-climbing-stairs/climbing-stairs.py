#
class Solution(object):
    
    def climbStairs(self, n):
      self.dp=[-1]*(n+1)
      def fun(n,dp):
         if n==0 or n==1:
            return 1
         if self.dp[n]!=-1:
           return self.dp[n]
         self.dp[n]= fun(n-1,dp)+ fun(n-2,dp)
         return self.dp[n]     
      return fun(n,self.dp)   