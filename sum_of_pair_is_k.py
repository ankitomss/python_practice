#function to find in the given array whether there exit possible pairs whose sum is divided by given K.
#return 1 if true else 0


def finddivisors(sum_array):
	divisors=[]
	for i in range(2,sum_array/2+1):
		if(sum_array%i==0):
			divisors.append(i)
	
	return divisors




def ispairs_possible(numbers):
	temp=0
	sum_array=0
	done=0

	if(len(numbers)%2!=0):
		return 0

	for i in range(len(numbers)):
		for j in range(len(numbers)):
			if(i==0):
				sum_array=sum_array+numbers[j]

			if(numbers[i]<numbers[j]):
				temp=numbers[j]
				numbers[j]=numbers[i]
				numbers[i]=temp
	
	left=0;
	right=len(numbers)

	divisors = finddivisors(sum_array)
	flag=0
	for i in range(len(divisors)):
	
	while (left<right):
		numbers[left]+numbers[right]


	print sum_array
	print divisors
	print numbers

ispairs_possible([0,1,5,9,3,4])

