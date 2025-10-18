# for i in range(1, 20, 2):
#     print(i)    #hw 1

# a = input() #31
# z = 0
# for i in a: #поэлементно перебираем строку
#     z += int(i) #переводим символ '3' в число 3
# print(z) #4         #hw 2

# a = input("Enter: ").split(" ")
# z = False
# for i in a:
#     if int(i) > 100:
#         print(i)
#         z = True
#         break
# if z == False or z != True or not(z):
#     print("Таких чисел нет")      #hw 3

# a = int(input())
# b = False
# for i in range(2, a):
#     if a % i == 0:
#         b = True
#         print(i)
#         break
# if not(b):
#     print("Число простое")     #hw 4

# for i in range(1, 5):
#     for j in range((4 -i), -1, -1):
#         print('*' * i + " " * j)
#         break      #hw 5




# num = int(input("Enter a number: "))
# found = False
# for i in range(2, num):
#     if num % i == 0:
#         found = True
#         print("Составное число")
#         break
# if not found:
#     print("Простое число")      #1 task



# num = int(input("Enter a number: "))
# if num < 3:
#     print("Таких чисел нет")
# else:
#     result = (num // 3) * 3
#     print(result)      #2 task



#in - в условиях проверяет принадлежность
#end - устанавливаем свой символ в конце по умолчанию \n
# a = input("Введите строку: ")
# b = "aieouyAIEOUY"
# for i in a:
#     if i not in b:
#         print(i, end="")      #3 task



# for i in range(3, -1, -1):
#     print("*" * (4 - i) + " " * i)
# for i in range(3, 0, -1):
#     print("*" * i + " " * (4 - i))     #4 task




















































