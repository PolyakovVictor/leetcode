class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.split(" ")
        s2 = s.split()
        print(s1, s2)

        if not s:
            return s

        elif len(s[-1]) > 0:
            return len(s[-1])

        while len(s[-1]) == 0:
            print(len(s[-1]), s[-1:])
            s = s[:-1]

        return len(s[-1])


cls = Solution()
print(cls.lengthOfLastWord("    Hello World  "))
