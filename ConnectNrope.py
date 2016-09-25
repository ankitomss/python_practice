import heapq
def connectRopes(nums):

    cost=0
    heapq.heapify(nums)
    while len(nums)!=1:
        x, y=heapq.heappop(nums), heapq.heappop(nums)
        heapq.heappush(nums, x+y)
        cost+=x+y

    return cost


nums=[4, 3, 2, 6]
print connectRopes(nums)