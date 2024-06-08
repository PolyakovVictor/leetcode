class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            for i in range(len(haystack)):
                if needle in haystack[:i+len(needle)]:
                    return i
        else:
            return -1


cls = Solution()
print(cls.strStr(haystack="hello", needle="ll"))
# haystack = "sadbutsad", needle = "sad"
