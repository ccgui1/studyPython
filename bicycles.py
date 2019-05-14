bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print()
print(bicycles[0].title())
name = "Ada lovelace"
print(bicycles[-1].title())
print(name.title())
print(name.upper()) #大写
print(name.lower()) #小写 

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)
print("********************************")
print("Hello, " + full_name.title() + "!")
print("********************************")
message = "Hello, " + full_name.title() + '!'
print(message)
print("********************************")
print("\tPython")
print("********************************")
print("Languages:\nPython\nC\nJaveScript")
print("********************************")
#rstrip()剔除末尾的空白
#lstrip()剔除开头的空白
#strip()剔除开头和末尾的空白
favorite_language = '   python '
print(favorite_language)
print(favorite_language.rstrip())
favorite_language = favorite_language.rstrip()
#print(favorite_language.lstrip())
print(favorite_language.strip())
print("********************************")


