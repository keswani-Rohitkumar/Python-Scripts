class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        cnt = 0
        n = len(s)
        for i in range(n-k+1):
            t = int(s[i:i+k])
            if t!=0 and num%t == 0:
                cnt+=1
            else:
                continue
        return cnt