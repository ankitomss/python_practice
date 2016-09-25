'''
the problem is simply finding a2+b2=c2, which is equal to find a+b=c
'''


def find(nums):
    nums = sorted(nums)
    nums = [pow(num, 2) for num in nums]
    print nums
    result = []
    for i in range(len(nums)-1, -1, -1):
        s, e = 0, i-1
        while s < e:
            total = nums[s] + nums[e]
            if total == nums[i]:
                result.append([nums[s], nums[e], nums[i]])
                s += 1
                e -= 1
            elif total < nums[i]:
                s += 1
            else:
                e -= 1

    return result


nums = [3, 1, 4, 6, 5]
print find(nums)
