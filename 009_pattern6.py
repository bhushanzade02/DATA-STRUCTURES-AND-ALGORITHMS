class Solution:
    def pattern6(self, n):
        n= n+1
        for i in range(1,n+1):
            for j in range(1,n-i+1):
                print(j, end = "")
            print()
