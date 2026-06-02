class Solution:
    def pattern18(self, n):
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for i in range(n):
            for j in range(n-i-1, n):
                if j != n-1:
                    print(alpha[j], end=" ")
                else:
                    print(alpha[j], end="")
            print()


# approach 2 
# alpha = list("ABCDEFGHIJKLMNOPQRSTUVW")
# # print(alpha)
# n = 5 
# for i in range(n):
#     for j in range(n-i-1,n):
#         print(alpha[j] , end = ' ')
#     print()




