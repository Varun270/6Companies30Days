def numDecodings(self, s: str) -> int:
        poss = {f'{i}' for i in range(1, 27)}
        dp = [0] * (len(s) + 2)
        dp[-2] = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] in poss:
                
                case1 = dp[i + 1]
                
                
                case2 = dp[i + 2] if s[i: i + 2] in poss else 0
                dp[i] = case1 + case2
            else:
                dp[i] = 0
        return dp[0]