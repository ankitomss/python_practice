hashmap={}

def make_hash(words):
	for i in words:
		hashmap[i] = 0
	return hashmap


def check_string(string):
	
	if(len(string)==0):
		return 1

	for i in range(len(string)):
		if(hashmap.has_key(string[:i+1])):
			return check_string(string[i+1:])



make_hash(["i", "like", "sam", "sung","mobile", "ice", "cream"])
print "now the answer is", check_string("ilike")
