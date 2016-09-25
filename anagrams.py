

def findanagrams(wordlist):

	hashmap = {}


	for i in range(len(wordlist)):
		asci = 0
		for j in range(len(wordlist[i])):
			asci = asci + ord(wordlist[i][j])
		hashmap[asci] = 0



	for i in range(len(wordlist)):
                asci = 0
                for j in range(len(wordlist[i])):
                        asci = asci + ord(wordlist[i][j])
                hashmap[asci] = hashmap[asci] + 1

	for i in range(len(wordlist)):
                asci = 0
                for j in range(len(wordlist[i])):
                        asci = asci + ord(wordlist[i][j])
               	print wordlist[i], "is having these many anagrams", hashmap[asci]


findanagrams(["cat", "dog", "tac", "god", "act"])
