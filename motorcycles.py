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
print("*****************************")
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
print("*****************************")
last_owned = motorcycles.pop()
print("The last motorcycles I owned was a " + last_owned.title() + '.') 
 ##pop()可删除列表中任何位置的元素，在括号中指定位置
print("*****************************")
motorcycles = ['honda','yamada','suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

#根据值删除元素
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

#motorcycles.remove('ducati')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")








