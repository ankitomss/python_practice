class Solution(object):
    def findindex(self, sort, num):
        s, e=0, len(sort)-1
        while s<=e:
            m=(s+e)/2
            if s==e:
                return (s+1 if num > sort[s] else s)
            elif sort[m]==num:
                return m-1
            elif sort[m] < num:
                s=m+1
            elif sort[m] > num:
                e=m-1


        return s


    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        if n==0: return []
        sort=[nums[n-1]]
        ans=[0]*n
        for i in range(n-2,-1,-1):
            index=self.findindex(sort, nums[i])
            sort.insert(index, nums[i])
            ans[i]=index

        return ans

s=Solution()
nums=[26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
print s.countSmaller(nums)
