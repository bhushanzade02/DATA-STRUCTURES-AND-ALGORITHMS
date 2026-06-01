class Solution:
    def pattern16(self, n):
        alpha = list("ABCDEFGHIJKLMNOPQRSTUVWX")
        for i in range(n):
            for j in range(-1,i):
                print(alpha[i], end = "")
            print()
