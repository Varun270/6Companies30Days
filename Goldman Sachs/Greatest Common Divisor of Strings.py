class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        str1Length, str2Length = len(str1), len(str2)
        
        if str2Length > str1Length: 
            return self.gcdOfStrings(str2, str1)
        
        if str1[:str2Length] == str2: 
		
            if str1Length == str2Length: 
                return str2
            
            return self.gcdOfStrings(str2, str1[str2Length:]) 

        return ""