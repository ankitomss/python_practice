
def permutations(word):
	if len(word)<=1:
		return [word]


	perms=permutations(word[1:])
	char=word[0]
	result=[]

	for perm in perms:
		for i in range(len(perm)+1):
			result.append(perm[:i]+char+perm[i:])
	
	# for item in result:
     #    	print item

	return result
	
	

def combinations(s, curstr, k, result):
	if not k:
		result.append(curstr)
		return
	if not s:
		return

	for i in range(len(s)):
		combinations(s[i+1:],curstr+s[i], k-1, result)
		# combinations(s[i+1:],curstr, k, result)


def permut(s, curstr, result):
	if not s:
		result.append(curstr)
		return

	for i in range(len(s)):
		permut(s[:i]+s[i+1:], curstr+s[i], result)


permutations("ankit")
result=[]
#combinations("ankit", "", 3, result)
permut("ankit", "", result)
print result, len(result)

