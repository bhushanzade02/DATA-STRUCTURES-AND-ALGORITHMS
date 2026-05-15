class Solution:
    def forLoop(self, low : int, high : int) -> int:
        total = low 
        for i in range(low + 1 , high + 1 ):
            total += i 
        return total 
