def maxProfit(self, K, N, A):
        profit = [[0 for i in range(N + 1)] 
                 for j in range(K + 1)] 

        # Fill the table in bottom-up fashion 
        for i in range(1, K + 1): 
            prevDiff = float('-inf')
            
            for j in range(1, N): 
                prevDiff = max(prevDiff,
                               profit[i - 1][j - 1] - 
                               price[j - 1]) 
                profit[i][j] = max(profit[i][j - 1], 
                                   price[j] + prevDiff) 
    
        return profit[K][N - 1]