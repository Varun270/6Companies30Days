def sots(self,arr):
        n=len(arr)
        for i in range(n):
            min_indx=i
            for j in range(i+1,n):
                if arr[min_indx]>arr[j]:
                    min_indx=j
            arr[i],arr[min_indx]=arr[min_indx],arr[i]
        return arr

	def matchPairs(self,nuts, bolts, n):
		self.sots(nuts)
        self.sots(bolts)