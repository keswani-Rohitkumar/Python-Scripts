class Solution:
    # def numOfSubarrays(self, arr, k, threshold):
    #     cnt = 0
    #     l = len(arr)
    #     m = threshold * k
    #     for i in range(l-k+1):
    #         x = arr[i:i+k]
    #         if sum(x) >= m:
    #             cnt +=1
    #     return cnt

#
#  Updated sliding window logic where we perform sum in sliding window compare to the above logic where we perform sum after the sliding window.
    def numOfSubarrays(self, arr, k, threshold):
        cnt = 0
        l = len(arr)
        s = sum(arr[:k])
        m = threshold * k
        if s >= m:
            cnt+=1 
        for i in range(l-k):
            s =  s - arr[i] + arr[i+k]
            if s >= m:
                cnt +=1
        return cnt

s = Solution()
print(s.numOfSubarrays([2,2,2,2,5,5,5,8], 3,4))