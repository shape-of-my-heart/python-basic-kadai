class Human:

   def __init__(printinfo, name, age):
     printinfo.name = name
     printinfo.age = age

   def set_name(printinfo, name, age):
     printinfo.name = name
     printinfo.age = age

   def show_name(printinfo):
     print(printinfo.name)
     print(printinfo.age)

human = Human("名前","年齢")

print(human.name)
print(human.age)
