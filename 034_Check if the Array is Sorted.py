class Solution:
    def arraySortedOrNot(self, arr, n):
          for i in range(n):
            if arr[i] < arr[i+1]:
                return True
            else :
                return False
