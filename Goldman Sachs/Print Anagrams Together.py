from collections import defaultdict

class Solution:
    def Anagrams(self, words, n):
        
        
        res = defaultdict(list)
        
        for s in words:
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord("a")] += 1
                
            res[tuple(count)].append(s)
            
        return res.values()