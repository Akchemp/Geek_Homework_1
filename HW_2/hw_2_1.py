# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


my_int = 5
my_float = 1.98
my_str = "Hello World"
my_list = ["Michael Jordan", 23]
my_tuple = ("Magic Johnson", 32)
my_dict = {"NBA": "Team Chicago Bulls", "city": "Chicago"}

full_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in full_list:
    print(f"{i} is {type(i)}")
