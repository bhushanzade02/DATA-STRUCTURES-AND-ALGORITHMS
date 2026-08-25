class Solution:
    def divisors(self, n):
        fc = []
        for i in range(1,n+1):
            if n % i == 0 :
                fc.append(i)
        return (fc)
