n=5
num = "ABCDEFGHIJKLMNOP"
ls = list(num)
for i in range(n,0,-1):
    for j in range(i):
        print(ls[j], end =' ')
        j-=1
    print()
