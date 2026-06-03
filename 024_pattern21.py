class Solution:
    def pattern21(self, n):
        print("*"*n)
        for i in range(n-2):
            print("*", end = '')
            print(" "*(n-2), end = '')
            print("*")
        print("*"*n)
