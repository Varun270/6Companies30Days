def canPair(self, arr, k):
		dic = defaultdict(int)
	    count = 0
	    l = len(arr)
	    for n in arr:
		    m = n%k
		    alt = 0 if m==0 else k-m

		    if dic[alt]>0:
			    dic[alt]-=1
			    count+=2
		    else:
			    dic[m]+=1
	    return count==l