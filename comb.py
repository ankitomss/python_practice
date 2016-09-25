# def comb(nums, k, curls, result):
#
#     if k==0:
#         print curls
#         result.append(curls)
#         return
#
#     for i in range(len(nums)):
#         comb(nums[i+1:], k-1, curls+[nums[i]], result)
#

def comb(nums, k, curls, result):
    if k==0:
        result.append(curls)
        return

    for i in range(len(nums)):
        comb(nums[i+1:], k-1, curls+[nums[i]], result)


nums=[1,2,3,4,5,6,7]
curls, result=[], []
comb(nums,3,curls, result)
print "total", len(result)
print result