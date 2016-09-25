
def learnPython():
	print("this is learning of python")
	a=0
	b=1
	c=a+b
	print(c)
	for i in range(12):
		print i
	
	fruits = ['banana', 'mango', 'apple']

	for name in fruits:
		print name
	for index in range(len(fruits)):
		print fruits[index]
	for index in range(10,20):
		if index % 2 == 0:
			print 'this is even'
		else:
			print 'this is odd'
	
	count =0
	while(count < 9):
		count=count+1
		print 'count is now', count


learnPython()
