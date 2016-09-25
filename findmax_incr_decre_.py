def findmax(nums):
	n=len(nums)
	l,r=0,n-1

	while l<=r:
		m=(l+r)/2
		if l==r:
			return nums[l]
		elif nums[m] > nums[m+1] and nums[m] > nums[m-1]:
			return nums[m]
		elif l+1==r:
			temp=nums[m] if nums[m] > nums[m+1] else nums[m+1]
			return temp
		elif nums[m] > nums[m-1]:
			l=m+1
		elif nums[m] > nums[m+1]:
			r=m-1


nums=[1,3,50,10,9,7,6]
print findmax(nums)
