motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
 #修改列表元素
print("*****************************")
motorcycles[0] = 'ducati'
print(motorcycles)
 #在列表中添加元素
print("*****************************")
motorcycles.append('ducati')
print(motorcycles) 
print("*****************************")
motorcycles = []
motorcycles.append('honda') 
motorcycles.append('yamaha')
motorcycles.append('suzuki')  

print(motorcycles)
 #在列表中插入元素
print("*****************************")
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles) 

 #从列表中删除元素
print("*****************************")
motorcycles = ['honda','yamada','suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

 #使用pop()方法删除元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)








