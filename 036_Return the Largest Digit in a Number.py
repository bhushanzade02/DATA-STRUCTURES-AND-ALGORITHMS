class Solution:
    def largestDigit(self, n):
        ans = n %10
        ans2 = n // 10 
        if ans > ans2 :
            return ans
        else:
            return (ans2)
