num = "ABCDEFGHIJKLMNOP"
ls = list(num)
for i in range(n+1):
    for j in range(i+1):
        print(ls[j], end =' ')
    print()
