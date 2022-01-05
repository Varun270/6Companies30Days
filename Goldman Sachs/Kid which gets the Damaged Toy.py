def lastPosition(n, m, k):
	
	if (m <= n - k + 1):
	    return m + k - 1

	
	m = m - (n - k + 1)

	
	if(m % n == 0):
		return n
	
	return m % n


n = 8
m = 4
k = 4
print(lastPosition(n, m, k))


