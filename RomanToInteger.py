class Solution:
    def romanToInt(self, s):
        roman_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        res = 0
        prev = 0

        for ch in s:
            num = roman_map[ch]
            if num > prev:
                res +=   num - 2*prev
            else:
                res += num
            prev = num

        return res


obj = Solution()
print(obj.romanToInt(s="MCMXCIV"))
