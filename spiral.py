def spiral(nums):
	m,n=len(nums), len(nums[0])
	right,left, up, down=n-1, 0, 0, m-1

	while left<=right and up<=down:
		print nums[up][left:right+1]
		up+=1
		print [nums[i][right] for i in range(up, down+1)]
		right-=1
		print [nums[down][i] for i in range(right, left-1, -1)]
		down-=1
		print [nums[i][left] for i in range(down, up-1, -1)]
		left+=1

nums=[[1,2,3], [4, 5,6], [7,8,9]]
spiral(nums)
