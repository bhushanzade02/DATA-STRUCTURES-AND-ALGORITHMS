class Solution:
    def whileLoop(self, d : int) -> int:
        total= d
        sum = d
        i = d
        while i < 50 :
            total = total + 10 
            sum = sum + total 
            i += 1
        return sum 
