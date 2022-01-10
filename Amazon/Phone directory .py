def displayContacts(self, n, contact, s):
        # code here
        
        def insert(root ,word):
            
            temp = root
            for ch in word:
                
                if (ch not in temp.child):
                    temp.child[ch] = node()
                
                temp = temp.child[ch]
                temp.words.append(word)
            
            temp.end = 1
        
        def query(root):
            
            ans = []
            flag = 1
            temp = root
            for ch in s:
                
                if (ch not in temp.child) or (flag ==0):
                    ans.append([0])
                    flag = 0

                elif (flag):
                    
                    words = temp.child[ch].words
                    ans.append(words)
                    temp = temp.child[ch]
                    
            res = []
            
            for r in ans:
                
                vis = set()
                curr = []
                for w in sorted(r):
                    
                    if (w not in vis):
                        vis.add(w)
                        curr.append(w)
                
                res.append(curr)
            
            return (res)
                
            
            return (ans)
        
        root = node()
        root.end = 0
        
        for word in contact:
            
            insert(root ,word)
        
        size = len(s)
        
        ans = query(root)
        #print(ans)
        
        return ans