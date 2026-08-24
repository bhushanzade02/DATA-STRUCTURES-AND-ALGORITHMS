class Solution:
    def GCD(self, n1, n2):
        factors1 = []
        for i in range(1,n1+1):
            if n1 % i == 0 :
                factors1.append(i)
        print(factors1)
        factors2 = []
        for j in range( 1,n2+1):
            if n2 % j == 0:
                factors2.append(j)
        fact1 = factors2
        print(fact1)
        set1 = set(factors1)
        common_num = [num for num in fact1 if num in set1 ]
        return max(common_num)

