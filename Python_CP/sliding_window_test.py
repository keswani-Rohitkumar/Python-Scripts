arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)

window_sum = sum(arr[:k])
max_sum = window_sum
for i in range(5):
    window_sum = window_sum - arr[i] + arr[i + k]
    max_sum = max(window_sum, max_sum)
    
print(max_sum)
print("Github Check")

#Class for finding maximum average in subarray

# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         n = len(nums)
#         window_sum = sum(nums[:k])
#         max_sum = window_sum
#         for i in range(n-k):
#             window_sum = window_sum - nums[i] + nums[i+k]   
#             max_sum =  max(window_sum, max_sum)
#         return max_sum/k