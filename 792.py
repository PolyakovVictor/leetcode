from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        result = 0
        for i in words:
            s_pointer = 0
            w_pointer = 0
            while s_pointer < len(s) and w_pointer < len(i):
                if s[s_pointer] == i[w_pointer]:
                    w_pointer += 1
                    s_pointer += 1
                else:
                    s_pointer += 1
            if w_pointer == len(i):
                result += 1
        return result


cls = Solution()
print(cls.numMatchingSubseq(s="abcde", words=["a", "bb", "acd", "ace"]))
