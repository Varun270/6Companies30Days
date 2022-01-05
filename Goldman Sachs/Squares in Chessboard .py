def squaresInChessBoard(self, N):
        
        ans = 0
        for i in range(1, N+1):
            ans += i * i
        return ans 