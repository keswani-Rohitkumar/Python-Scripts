class Solution:
    def removeStars(self, s: str) -> str:
        x = [i for i in s]
        stack = []
        for i in x:
            if i == '*':
                stack.pop()
            else:
                stack.append(i)
        return "".join([str(i) for i in stack])

# a = Solution()
# print(a.removeStars("leet**cod*e"))