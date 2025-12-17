# a, b, c = input("Введите три значения: ").split()
# print("Значение переменной a: ", a)
# print("Значение переменной b: ", b)
# print("Значение переменной c: ", c)        #1 task



# spisok = input().split()
# a = int(spisok[0])
# b = int(spisok[1])
# c = int(spisok[2])
# d = int(spisok[3])
# print(a + c, b * d)        #2 task



# chislo = input()
# n_1 = int(chislo[0])
# n_2 = int(chislo[1])
# n_3 = int(chislo[2])
# n_4 = int(chislo[3])
# print("Произведение разрядов числа: ", n_1 * n_2 * n_3 * n_4)        #3 task



# chisla = input()
# n_1, n_2 = map(int, chisla.split())
# num_1 = n_1 + n_2 * 3
# num_2 = n_2 - (n_1 % 2)
# print("Первое число: ", num_1)
# print("Второе число: ", num_2)         #4 task



# num = int(input("Введите число: "))
# if num % 2 != 0:
#     print("Удвоенное число: ", num * 2)
# else:
#     print("Число без изменений: ", num)          #5 task



# chislo = int(input("Введите число от 100 до 999: "))
# first_num = chislo // 100
# last_num = chislo % 10
# if (last_num % 2 != 0) or (first_num % 2 == 0):
#     chislo += 1
# elif last_num in (3, 7, 9):
#     chislo -= 1
# print(chislo)          #6 task



# x = int(input("Введите значение x: "))
# if x > 0:
#     y = 3 * x + 1
#     print(y)
# elif x == 0:
#     y = x
#     print(y)
# else:
#     y = x ** 2 + 2
#     print(y)          #7 task



# chislo = input().strip()
# num = int(chislo, 16)
# new_num = bin(num)[2:]
# one = new_num.count('1')
# print("Введёное число в формате двоичной СС: ", new_num)
# print("Количество единиц: ", one)         #8 task



# chislo = input()
# n_1 = int(chislo[0])
# n_2 = int(chislo[1])
# n_3 = int(chislo[2])
# n_4 = int(chislo[3])
# n_5 = int(chislo[4])
# print("Введённое число: ", chislo)
# print("Сумма всех разрядов: ", n_1 + n_2 + n_3 + n_4 + n_5)         #9 task



# s = input("Введите две строки: ")
# line_1, line_2 = s.split(",")
# line_1, line_2 = line_1.strip(), line_2.strip()
# print("Первая строка: " , line_1)
# print("Вторая строка: " , line_2)
# ind = line_1.find(line_2)
# print("Первое вхождение подстроки: ", ind)
# new_line = line_1[10:-6]
# print("Подстрока: ", new_line)
# result_line = line_1[::-3]
# print("Каждый третий: ", result_line)          #10 task



# s = input()
# print("Исходная строка: ", s)
# w = s.split(" ")
# res_list = []
# c = 0
# while c < len(w):
#     res_list.append(w[c][::-1])
#     c += 1
# resultat = "".join(res_list)
# print("Изменённая: ", resultat)