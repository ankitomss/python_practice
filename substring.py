def isallfound(count, word):
	flag = 0
	for i in word:
		if count.get(i) > 0:
			flag = 0
			return flag
		else:
			flag = 1
	
	return flag


def findword(word, sentence):
	count={}
	print word, sentence
	
	for i in range(len(word)):
		count[word[i]] = 0 

	for i in range(len(word)):
		count[word[i]]= count[word[i]] + 1
	
	print count
	start=0
	end=0
	flag =0
	min_len = 0
	for i in range(len(sentence)):
		if count.get(sentence[i], "empty")!= "empty": 
			count[sentence[i]] = count[sentence[i]] - 1
			if flag == 0:
				start = i
				flag = 1
			end=i

		if isallfound(count, word) == 1:
			min_len = end - start
			break

	end = end+1
	print "starting point of start and end", start, end

	while end < len(sentence):
		if sentence[end] == sentence[start]:
			start = start + 1
			while count.get(sentence[start], "empty") == "empty":
				start = start + 1
			
			if min_len > end - start:
				min_len = end -start
		else:
			end=end+1

	print "minimum string length is", min_len
	print start, end
	print count

findword("tist","this is a test string")



	
