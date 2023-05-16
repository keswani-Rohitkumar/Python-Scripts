from heapq import heapify, heappop, heappush
import math
def minStoneSum(piles,  k) -> int:
        num = [-n for n in piles]
        heapify(num)
        #print(num)
        for i in range(k):
            x = heappop(num)
            x = math.floor(x/2)
            heappush(num,x)
            #print(num)
        return -sum(num)

print(minStoneSum([5,4,9], 2))