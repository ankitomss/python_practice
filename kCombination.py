def find(nums, curcomb, k, result):
	if len(curcomb)==k:
		result.append(curcomb)
		return

	if not nums:
		return


	find(nums[1:], curcomb, k, result)
	find(nums[1:], curcomb+str(nums[0]), k, result)


def kcomb(nums, k):
	result=[]
	find(nums, "", k, result) 	
	return result


nums=[1,2,3,4,5,6,7]
results=kcomb(nums, 3)

for result in results:
	print result

print "total", len(results)