class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s.split(' ')
        if s[-1]:
            return len(s[-1])
        else:
            return 0


cls = Solution()
print(cls.lengthOfLastWord(" luffy is still joyboy   "))
