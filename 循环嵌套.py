i = 0
while i < 5:
    j = 0
    while j < 5-i:
        print("* ",end="")
        j += 1
    print()
    i += 1

#打印乘法表
i = 1
while i < 10:
    j = 1
    while j < i+1:
        print(str(i) + '*' + str(j) + '=',j*i,end=" ")
        j += 1
    print()
    i += 1
