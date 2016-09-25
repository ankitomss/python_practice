def findmin(nums):

	s, e=0, len(nums)-1
	m=e/2
	while s<e:
		if m < e and nums[m+1] < nums[m]:
			return nums[m+1]
		elif m > s and nums[m] < nums[m-1]:
			return nums[m]
		elif nums[m] < nums[s]:
			e=m-1
		elif nums[m] > nums[s]:
			s=m+1
		m=(s+e)/2
	return nums[s]

nums=[3,4,1, 2]
print findmin(nums)
