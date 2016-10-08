import sys
class Solution(object):

    def solve(self, nums, m, memory, key, sumNums):
        key = key + "_" + str(m)

        if m == 1:
            ans = sumNums if nums else -1
            memory[key] = ans
            return ans
        elif not nums or m > len(nums):
            return -1

        if key in memory: return memory[key]

        total, ret = 0, [-1 for k in range(len(nums))]
        for i in range(len(nums)):
            total += nums[i]
            val = self.solve(nums[i+1:], m-1, memory, key[i+1:], sumNums - total)
            if val is not -1:
                ret[i] = max(total, val)

        ans = sys.maxint
        for x in ret:
            if x is not -1:
                ans = min(ans, x)

        memory[key] = ans

        return ans


    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        key, total = "".join(map(str, nums)), sum(nums)
        return self.solve(nums, m, {}, key, total)



