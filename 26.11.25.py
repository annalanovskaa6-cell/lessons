#ФУНКЦИИ
# for i in range(10):
#     print(i)
#
# for i in range(30):
#     print(i)

#аргументы - значения, принимаемые функцией
# def name_func(first_arg = 10, *,  second_arg = 15):   #функция
#     #тело функции
#     for i in range(first_arg, second_arg):
#         print(i)
    #конец тела функции
#Названия функций уникальны(строятся как переменные)

#параметры
# name_func(10, second_arg = 25)   #вызов функции
# name_func(second_arg = 25)
# name_func(first_arg = 5, second_arg = 25)

# def name_func_2(x, y, /):
#     print(x, y)
#     pass   #ничего (заглушка)
# name_func_2(x = 5, y = 5)
# name_func_2(5, 2)   #можно

# def name_func_3(*args):
#     for i in args:
#         print(i)
# name_func_3(1, 3, "world", 5, "hello")

# def name_func_4(**kwargs):   #kwargs - словарь
#     kwargs.pop("name2")
#     print(kwargs)
# name_func_4(name1 = 1000, name2 = 2)

# def a():
#     def b(x):
#         print(x + "world")
#     b("hello")
# a()


#x = 20   #глобальная область видимости
# def local_func():
#     global x
#     x = 10   #локальная область видимости
#     print(x)

# def local_func():
#     # global x
#     x = 10   #локальная область видимости
#     print(x)
#     return x, x, x #возвращаем значение
# print(local_func()[0] + 25)
# print(x)

# def a():
#     x = 10   #охватывающая область
#     def b():
#         nonlocal x
#         x = 5
#         print(x)
#     b()
#     print(x)
# a()

# def square(x):
#     while True:
#         if x == 5:
#             return
#         x += 1
#
# print(square(10))
# print(square(15))
# print(square(100))

# sum()

# x:int = 0
# def func(s:str) -> list:
#     """
#     Эта функция делает что-то
#     :return:
#     ничего
#     """
#     global x
#     while True:
#         while True:
#             if x >= 5:
#                 return[1, 2, 3]
#             x += 1
# print(func("hello"))
# print(x)



# type(x) == int -> isinstance(x, int)

# def division(x, y):
#     if y != 0 and type(x) == int and type(x) == int:
#         return x / y
#     return
# print(division(1, 2))          #1 task



# def is_even(n):
#     if n % 2 == 0:
#         return True
#     return False
# print(is_even(6))          #2 task