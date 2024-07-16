class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0
        while s_pointer < len(s) and t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                t_pointer += 1
            else:
                t_pointer += 1
        return True if s_pointer == len(s) else False


cls = Solution()
print(cls.isSubsequence(s="aaaaaa", t="bbaaaa"))
