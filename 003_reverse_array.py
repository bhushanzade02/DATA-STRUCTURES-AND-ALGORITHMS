class Solution:
    def reverse(self, arr: list) -> None:
        left = 0 
        right = len(arr)-1
        while left < right :
            arr[left] , arr[right] = arr[right] , arr[left]
            left = left + 1 
            right = right - 1 

# class Solution:
#     def reverse(self, arr: list) -> None:
#         arr[:] = arr[::-1]

            





