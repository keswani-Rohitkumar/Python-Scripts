arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)

window_sum = sum(arr[:k])
max_sum = window_sum
for i in range(5):
    window_sum = window_sum - arr[i] + arr[i + k]
    max_sum = max(window_sum, max_sum)
   
print(max_sum)