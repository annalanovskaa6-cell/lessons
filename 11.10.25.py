#a = 10 if 10 > 2 else 2      #цельная конструкция, else и if едины
#print(a)


#year = int(input("Введите год: "))
#if year % 4 == 0 and year// 100 != 0 or year % 400 == 0:
#    print("Високосный")
#else:
#   print("Не високосный")     #1 task



#chislo = int(input("Введите число: "))
#if chislo == 1:
#    r = int(input())
#    print("Площадь круга: ", 3.14 * r **2)
#elif chislo == 2:
#    a = int(input())
#    b = int(input())
#    print("Площадь элипса: ", 3.14 * a * b )
#else:
#    print("Error")     #2 task



# num = int(input("Enter a number: "))
# a = num % 10
# b = num // 100
# c = (num // 10) % 10
# count = 0
# if a % 2 == 0 or a % 5 == 0:
#     count += 1
# if b % 2 == 0 or b % 5 == 0:
#     count += 1
# if c % 2 == 0 or c % 5 == 0:
#     count += 1
#
# if count >= 2:
#     print(num)
# else:
#     print(num + 1)        #3 task



# num_1 = int(input("Enter the first number: "))
# num_2 = int(input("Enter the second number: "))
# num_3 = int(input("Enter the third number: "))
# if not(num_1 < num_2 + num_3 and num_2 < num_1 + num_3 and num_3 < num_1 + num_2):
#     print("Треугольник существует")
#
# elif num_1 == num_2 == num_3:
#     print("Треугольник равносторонний")
# elif num_1 == num_2 and num_3 != num_1:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")       #4 task



# month = int(input("Введите номер месяца: "))
# match month:
#     case 1 | 3 | 5 | 7 | 8 | 10 | 12:
#         print("31 день")
#     case 4 | 6 | 9 | 11:
#         print("30 дней")
#     case 2:
#         print("28 дней")      #5 task



# input_str = input()
# input_num = int(input())
# match (input_str, input_num):
#     case("Рабочий", t) if 9 <= t <= 18:
#         print("Рабочее время")
#     case("Выходной", t) if 10 <= t <= 16:
#         print("Рабочее время")
#     case("Праздничный", a):
#         print("Не работает")
#     case _:
#         print("Ошибка ввода")      #6 task










