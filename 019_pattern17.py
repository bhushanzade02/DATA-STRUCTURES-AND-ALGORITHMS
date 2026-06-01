class Solution:
    def pattern17(self, n):
        alpha = list("ABCDEFGHIJKLMNOPQRSTUVWX")

        for i in range(n):
            for j in range(n-i-1):
                print(" ",end = '')
            for j in range(0,i):
                print(alpha[j] , end = "")
            for j in range(i,-1,-1):
                print(alpha[j], end = "")
            # for j in range (n-i-1):
            #     print("-", end = '')
            print()

    
