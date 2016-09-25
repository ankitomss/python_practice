def LCS(s1, s2):
	m=len(s1)
	n=len(s2)
	dp=[[0 for i in range(n+1)] for j in range(m+1)]
	b=[["" for i in range(n+1)] for j in range(m+1)]
	for i in range(1,m+1):
		for j in range(1,n+1):
			if s1[i-1]==s2[j-1]:
				dp[i][j]=dp[i-1][j-1]+1
				b[i][j]="diagonal"
			else:
				dp[i][j]=max(dp[i-1][j],dp[i][j-1])
				if dp[i-1][j]>=dp[i][j-1]:
					b[i][j]='up'
				else:
					b[i][j]='down'
	#print dp	
	print dp[m][n]
	return b

s1="10010101"
s2="010110110"
s3="101"
s4="011"
b=LCS(s1,s2)
print b
def printlcs(b, s1, i, j):
	if i==0 and j==0:
		return
	if b[i][j]=="diagonal":
		printlcs(b, s1, i-1,j-1)
		print s1[i]
	elif b[i][j]=="up":
		printlcs(b, s1, i-1, j)
	else:
		printlcs(b, s1, i, j-1)

printlcs(b, s1, len(s1), len(s2))
