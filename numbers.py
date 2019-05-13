#range()函数
print("******************************")
for value in range(1,5):
	print(value)
numbers = list(range(1,6))
print(numbers)
#range(2,11,2)中从2开始数，然后不断加2，直至到达或超过终值11
print("******************************")
even_numbers = list(range(2,11,2))
print(even_numbers )
#将前10个整数的平方加入到一个列表中
print("******************************")
squares = []
for value in range(1,11):
#	square = value**2
	squares.append(value**2)
print(squares)
print("******************************")
digits = []
for digit in range(0,10):
	digits.append(digit)
#digits = range(0,10)
print(digits)
#求数字列表的最大值
print(max(digits))
#求数字列表的最小值
print(min(digits))
#求数字列表的总和
print(sum(digits))
#另一法
print("******************************")
squares = [value**2 for value in range(1,11)]
print(squares)
