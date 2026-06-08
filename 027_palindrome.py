class Solution:
    def isPalindrome(self, n):
        n = str(n)
        
        c = n == n[::-1]
        return (c)
