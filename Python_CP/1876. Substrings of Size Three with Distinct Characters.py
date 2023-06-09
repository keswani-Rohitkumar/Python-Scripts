class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cnt = 0
        n = len(s)

        for i in range(n-2):
            t = set(s[i:i+3])
            if len(t) == 3:
                cnt +=1
        return cnt



        # Sliding window logic but can be efficient

        # s = [i for i in s]
        # n = len(s)
        # cnt = 0
        # x= s[:3]
        # if len(set(x)) == 3:
        #     cnt +=1
        # for i in range(3,len(s)):
            
        #     x = x[1:]
        #     x.append(s[i])

        #     if len(set(x)) == 3:
        #         cnt +=1
        #     else:
        #         cnt += 0

        #     print(len(set(x)))
        #     print(x)
        #     #set(x)
            
            
        
        return cnt