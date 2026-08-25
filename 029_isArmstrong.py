class Solution:
    def isArmstrong(self, n):
        gr_truth = n
        add = 0
        string = str(n)
        while n > 0 :
            num = n %10
            # print("rem",num)
            fc = num **3
            # print("fc",fc)
            add +=fc
            # print("add ",add)
            n = n //10
        # print(add)
        if gr_truth == add :
            return True
        else :
            return False
