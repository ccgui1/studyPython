i = 100;
while i < 1000:
    a = i // 100
    b = i //10 % 10
    c = i % 10
    d = a**3 + b**3 + c**3
  # print(str(i) + " " + str(a) +"//" + str(b) + "//" + str(c))
    if i == d:
        print(i)
    i += 1

# 判断是否为质数 法一
num = int(input("请输入任意一个大于1的整数："))
print(num)
n = 2
while n < num:
    if num % n == 0:
        print(str(num) + "不是质数")
        break
    elif num % n != 0 and n >= num-1:
        print(str(num) + "是质数")
    n += 1

#法二
falg = True
while n < num: 
    if num % n == 0:
        falg = False
    n += 1
if falg:
    print(str(num) + "是质数")
else:
    print(str(num) + "不是质数")
