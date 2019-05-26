employee = []
a = 0
while True:
    print()
    print('='*10 + '欢迎使用员工管理系统' + '='*10)
    print('请选择你要做的操作:\n\t1、查询员工\n\t2、添加员工\n\t3、删除员工\n\t4、退出系统')
    number = input('请选择（1-4）')
    if number == '1':
        print('='*15)
        print('序号    姓名    年龄   性别    住址')
        for i in range(len(employee)):
            if a == 0:
                print(employee[i],end='     ')
            elif (a+1) % 6 == 0 and a != 0:
                print(employee[i],end='')
            else:
                print(employee[i],end='     ')
            a += 1
    elif number == '2':
        print('='*15)
        emp_num = input('请输入员工序号：')
        employee.append(emp_num)
        emp_name = input('请输入员工姓名：')
        employee.append(emp_name)
        emp_age = input('请输入员工年龄：')
        employee.append(emp_age)
        emp_sex = input('请输入员工性别：')
        employee.append(emp_sex)
        emp_add = input('请输入员工地址：')
        employee.append(emp_add)
        employee.append('\n')

    elif number == '3':
        del_emp_num = input('请输入删除的员工号：')
        num = employee.index(del_emp_num)
        # print(num)
        employee[num:num + 6] = []
    if number == '4':
        break
