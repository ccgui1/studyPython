import random
print("欢迎光临本游戏")
print("请选择你的身份：\n1.唐僧\n2.白骨精")
id = input('请选择【1-2】')
if id == 1:
    print("你将以唐僧的身份进行游戏")
    id = 1
elif id == 2:
    print("你他妈就只能以唐僧进行游戏")
    id = 1
else:
    print("你他妈就只能以唐僧进行游戏")
    id = 1
health_point=2
attack_point=2
global a
a = random.randint(0,10)
print(a)
while True:
    print('*'*30)
    print("你现在的攻击值为",health_point,"生命力为",attack_point)
    new_id = 0
    print("请选择你现在要进行的任务:\n1.练级\n2.打boss\n3.逃跑")
    task_id = input()
    if task_id == '1':
        health_point += 2
        attack_point += 2
        a += 0.2
       # print("你现在的攻击值为",health_point,"生命力为",attack_point)
    elif task_id == '2':
        if a >= 10:
            print("现在a的值",a)
            print("你击败boss")
        else:
            print("你被boss击败")
            print("现在a的值",a)
    elif task_id == '3':
        break
