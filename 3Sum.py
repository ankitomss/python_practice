class Solution(object):
    def sum3(self, nums, sum):
        nums=sorted(nums)
        print nums
        n=len(nums)
        ls=[[]]
        for i in range(n-2):
            while i>0 and i<n-2 and nums[i]==nums[i-1]: i+=1
            s, e=i+1, n-1

            while s<e:
                check=nums[i]+nums[s]+nums[e]
                if check==sum:
                    ls.append([nums[i], nums[s], nums[e]])
                    s+=1
                    e-=1
                    while s<e and nums[s]==nums[s-1]:s+=1
                    while s<e and nums[e]==nums[e+1]:e-=1
                elif check<sum:
                    s+=1
                elif check>sum:
                    e-=1
        return ls

nums=[-1, 0, 1, 2, -1, -4]
print Solution().sum3(nums, 0)






