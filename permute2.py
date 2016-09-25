def permute(word, curword):
	if not word:
		print curword
		return 


	for i in range(len(word)):
		permute(word[:i]+word[i+1:], curword+word[i])
	

permute("ankit","")
