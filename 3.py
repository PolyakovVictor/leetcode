class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = max_lenght = current_lenght = 0
        hash_table = {}

        for i in range(len(s)):
            if s[i] in hash_table and i >= start:
                start = hash_table[s[i]] + 1

            hash_table[s[i]] = i

            max_lenght = max(max_lenght, i - start + 1)

        return max_lenght


obj = Solution()

result = obj.lengthOfLongestSubstring(s="abcabcbb")

print(result)
