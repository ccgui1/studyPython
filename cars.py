#使用sort（）方法对列表进行永久性排序
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
#使用函数sort(reverse=True)进行反向排序
print("********************************")
cars.sort(reverse=True)
print(cars)

#使用函数sorted()进行临时排序
print("********************************")
cars = ['bmw','audi','toyota','subaru']
print("Here is the original list: ")
print(cars)
#倒着打印列表
print("********************************")
cars = ['bmw','audi','toyota','subaru']
print(cars)

cars.reverse()
print(cars)
#确定列表的长度
print("********************************")
cars = ['bmw','audi','toyota','subaru']
print(len(cars))
print(cars[-1])




