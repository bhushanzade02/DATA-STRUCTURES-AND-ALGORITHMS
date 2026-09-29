class Solution:
    def reverse(self, arr: list, n: int) -> None:
        s= len(arr)
        for i in range(s//2):
            arr[i],arr[s-1-i]= arr[s-1-i],arr[i]
        return (arr)
