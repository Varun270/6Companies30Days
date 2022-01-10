def max_of_subarrays(self,arr,n,k):
        
        i = 0
        ans = []
        while k != len(arr) + 1:
            ans.append(max(arr[i:k]))
            i += 1
            k += 1
        
        return ans