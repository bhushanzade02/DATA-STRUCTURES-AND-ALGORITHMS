class Solution:
    def pattern13(self, n):
        num = 1 
        for i in range(1,n+1):

        #  i= 1   print 1
        #  i = 2   print 1 2 
        #  i = 3   print 1 2 3 

            for j in range(1,i+1):
                print(num, end= " ")
                num += 1
            print()
