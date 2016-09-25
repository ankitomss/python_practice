class Solution(object):

    def findmax(self, nums):
        n=len(nums)
        if n==2:
            return nums[0]*nums[1] + max(nums[0], nums[1])
        _max=1
        
        for i in range(n):
            temp=self.findmax(nums[:i]+nums[i+1:])
            if i==0:
                temp=nums[i]*nums[i+1]+temp
            elif i==n-1:
                temp=nums[i]*nums[i-1]+temp
            else:
                temp=nums[i-1] *nums[i]*nums[i+1]+ temp
            _max=max(_max, temp)
        return _max

    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1: return nums[0]
        return self.findmax(nums)

nums=[35,16,83,87,84,59,48,41,20,54]
b=Solution()
print b.maxCoins(nums)
