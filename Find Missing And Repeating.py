def findTwoElement( self,arr, n): 
        i = 0
        ans = []
        
        while i < len(arr):
            correct_index = arr[i] - 1
            if arr[i] != arr[correct_index]:
                arr[i], arr[correct_index] = arr[correct_index], arr[i]
                
            i += 1
            
        for j in range(len(arr)):
            if arr[j] != j + 1:
                ans.append(arr[j])
                ans.append(arr[j] - 1)
                
        return ans