def skipMdeleteN(self, head, M, N):
        
        curr = head
        
        # The main loop that traverses through the
        # whole list
        while(curr):
            # Skip M nodes
            for count in range(1, M):
                if curr is None:
                    return 
                curr = curr.next
                    
            if curr is None :
                return 

            # Start from next node and delete N nodes
            t = curr.next 
            for count in range(1, N+1):
                if t is None:
                    break
                t = t.next
    
            # Link the previous list with remaining nodes
            curr.next = t
            # Set Current pointer for next iteration
            curr = t 