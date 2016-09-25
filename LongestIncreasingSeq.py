def LongestIncreasingSeq(s1):
	n=len(s1)
	dp=[1 for i in range(n)]

	for i in range(1,n):
		_max=1
		for j in range(i):
			
			if s1[i]>s1[j]:
				temp=dp[j]+1
			else:
				temp=1
			_max=max(temp,_max)
		dp[i]=_max
	globalmax=1
	for i in range(n):
		globalmax=max(globalmax,dp[i])
	print dp	
	print globalmax

s1=[1,6,2,5,3,2,0]
LongestIncreasingSeq(s1)

	
