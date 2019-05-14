class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
    def fill_gas_tank(self):
        print("this car need a gas tank！")



class ElectricCar(Car):
    def __init__(self,make,model,year):          #初始化父类的属性
        super().__init__(make,model,year)
        self.batter_size = 70                #初始化电动汽车的特有属性
    def describe_battery(self):                      #打印一条描述电瓶容量的消息
        print("This car has a " + str(self.batter_size) + "-KWh Battery.")
    def fill_gas_tank(self):                         #重写父类
        print("This car doesn't need a gas tank")
my_new_car = Car('bwm','s','2020')
my_new_car.fill_gas_tank()

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()


















