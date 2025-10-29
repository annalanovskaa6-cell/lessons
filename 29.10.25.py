#math - библиотека для математических вычислений
#random - библиотека для генерации псевдослучайных чисел

import math    #импортируем модуль (как коробку)
from math import sqrt    #импортируем инструмент from math
import math as mth    #меняем название модуля и импортируем

# import math
# print(math.sqrt(25))   #sqrt - извлечение корня

from math import pow, sqrt
# from math import *   #* - все инструменты из модуля
# print(pow(10, 10))   #pow - возводит в степень

# import math as mth
# print(mth.pow(10, 10))


# from random import randint, choice
# index = randint(0, 4)   #от какого до какого числа сделать
# l = ["a", "b", "c", "d", "e"]
# print(choice(l))   #choice - рандомно выбирает элемент




# s = input("Введите вашу строку: ")
# a = len(s) // 2
# half_1 = s[:a]
# half_2 = s[a:]
# print(half_2 + half_1)     #1 task



# s = input("Введите вашу строку: ")
# j = s[::2]
# k = s[1::2][::-1]    #шаг "-1" - обратный порядок
# print(j + k)        #2 task



# s = input("Введите вашу строку: ")
# for i in range(0, len(s) - 2):
#     print(s[i : i + 3])      #3 task



# s = "шалаш, камыш, заказ, возврат, поиск, довод, спектр, комок, альянс"
# s = s.split(", ")
# for i in s:
#     if i == i[::-1]:
#         print(i)      #4 task



a = input("Введите вашу строку: ")
alpha = ""
amount = 0
#set - уникализирует список
for i in set(a):
    count = a.count(i)
    if count > amount:
        alpha = i
        amount = count
print(alpha, amount)
print(a[::3])
maximum = 0
indexes = ""
for i in set(a):
    if a.count(i) == 1:
        continue
    backward = a.rfind(i)
    forward = a.find(i)
    if (backward - forward) > maximum:
        maximum = backward - forward
        indexes = a[backward : forward]
print(indexes)      #5 task













