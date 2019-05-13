class Dog():
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def sit(self):
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		print(self.name.title() + " rolled over!")

	def name1(self):
		print("My dog's name is " + self.name.title())


my_dog = Dog('willes',6)
your_dog = Dog('lucy',3)
#print("My dog's name is " + my_dog.name.title() + ".")
#print("My dog is " + str(my_dog.age) + " years old.")

my_dog.name1()
my_dog.sit()
my_dog.roll_over()

#编写一个餐厅的类
print("*******************************")
print("\nyour dog's name is " + your_dog.name.title() + ".")
print("Your dog is  " + str(your_dog.age) + " years old.") 
your_dog.sit()


class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant = restaurant_name
		self.cuisine = cuisine_type
	def describe_restaurant(self):
		print(self.restaurant + ' ' + str(self.cuisine))
	def open_restaurant(self):
		print("This restaurant is opening!")	
		
my_restaurant = Restaurant('new east',2)
my_restaurant.open_restaurant()
my_restaurant.describe_restaurant()
first_restaurant = Restaurant('happy','www')
second_restaurant = Restaurant('unhappy','qwq')
first_restaurant.describe_restaurant()
second_restaurant.describe_restaurant()

print("*******************************")
class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
#"""判定更新的里程,防止被人往回调数据""" 
	def update_odometer(self,milleage):
		if milleage >= self.odometer_reading:
			self.odometer_reading = milleage
		else:
			print("You can't roll back an odometer!")	
#   """将里程表读数增加指定的量"""
	def increment_odometer(self,miles):
		self.odometer_reading += miles
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(23)
my_new_car.read_odometer()
update_odometer = int(input())
my_new_car.update_odometer(update_odometer)
my_new_car.read_odometer()

print("************************************")
my_used_car = Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name()) 

my_used_car.update_odometer(99999999)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()



















