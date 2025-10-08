#+ (сложение),- (вычитание),/ (деление),* (умножение)

#% (остаток от деления)
#print(3%2)
# // (целочисленное деление)
#print(5//2)
# () (объединение)
#print((1+2) * 2)
# ** (возведение в степень)
#print(10**2)

#and - логическое и
#print(1 and 1)
#or - логическое или
#print(True or 0)
#not - не
#print(not(True))

#числа и объекты
#== - сравнение (эквивалентность)
#print(True == True)
#!= - сравнение (отрицание)
#print(5 != 5)

#числа
#>=, <=, <, >
#print(10 >= 10)


#is_whether = bool(input("Идёт ли дождь? : "))
#if is_whether:
#   print("Да, идёт")

#is_whether = input("Идёт ли дождь? : ")
#if is_whether == "yes":
#    print("Да, идёт")
#elif is_whether == "no":   #срабатывает, если не сработал if
#   print("Нет, не идёт")
#else:  #действие срабатывает, если не сработали предыдущие
#    print("МБ нет или МБ да")

#a = input("Введите слово: ")
#match a:
#    case "no":
#        print("Почему нет")
#    case "yes":
#        print("Почему да")
#    case _:
#         print("Любые символы")



#a = int(input("Введите число: "))
#if a % 2 == 0:
#    print("Чётное")
#else:
#    print("Нечётное")     #1 task


#num = int(input("Введите число: "))
#if num > 0 and num % 2 == 0 and num % 10 != 0:
#    print("Положительное и чётное")
#elif num > 0 and num % 2 != 0:
#    print("Положительное и нечётное")
#elif num > 0 and num % 10 == 0:
#    print("Положительное и оканчивается на 0")
#else:
#    print("Отрицательное")     #2 task


num = int(input("Введите число: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)      #3 task




