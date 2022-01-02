def encode(arr):
    
    ans = ""
    curr_ele = arr[0]
    n = len(arr)
    count = 1
    
    for i in range(1, n):
        if arr[i] == curr_ele:
            count += 1
            
        else:
            ans += curr_ele + str(count)
            
            curr_ele = arr[i]
            count = 1
            
    ans = ans + curr_ele + str(count)
    return ans