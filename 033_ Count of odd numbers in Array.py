class Solution:
    def countOdd(self, arr, n):
        abb = []
        for i in arr:
            if i % 2 != 0:
                abb.append(i)
                # print("odd")
        return (len(abb))
