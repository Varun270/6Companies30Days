def countWays(self,m):
        
        mod = 1000000007
        
        dp=[0]*(m+1)
        dp[1]=1
        for i in range(2,m+1):
            if (i % 2 == 0):
                dp[i]=(dp[i-1]+1)%mod
            else:
                dp[i]=(dp[i-1]) % mod
        return (dp[m])%mod