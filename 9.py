class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x[::-1] == x


obj = Solution()

result = obj.isPalindrome(x=121)

print(result)
