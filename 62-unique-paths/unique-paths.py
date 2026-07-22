'''class Solution(object):
    
    def uniquePaths(self, m, n):
        dp=[[-1 for _ in range(n)]for _ in range(m)]
        def fun(i,j):
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            
            up=fun(i-1, j)
            left= fun( i, j-1)   
            dp[i][j]= up+left

            return dp[i][j]
        return fun[i-1][j-1]'''

class Solution(object):

    def uniquePaths(self, m, n):
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def fun(i, j):
            if i == 0 and j == 0:
                return 1

            if i < 0 or j < 0:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            up = fun(i-1, j)
            left = fun(i, j-1)

            dp[i][j] = up + left
            return dp[i][j]

        return fun(m-1, n-1)
