# a = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
# b = ""
# for i in a:
#     for j in a:
#         for k in a:
#             b = i + j + k
#             print(b)         #hw 1

# while True:
#     a = int(float(input()))
#     b = int(float(input()))
#     event = input()
#     if event == 'stop':
#         break
#     if event == '*':
#         print(a * b)
#     elif event == '**':
#         print(a ** b)
#     elif event == '+':
#         print(a + b)
#     elif event == '-':
#         print(a - b)
#     elif event == '/':
#         print(a / b)        #hw 3

# a = input()
# b = ""
# for i in a:
#     b = i + b
#     print(b)
# print("палиндром" if b == a else "не палиндром")       #hw 4




# a = [
#     [1, 2],
#     [3, 4]
# ]
#[3, 1],
#[4, 2]
#нужно создать пустой список
# print(a[0])
# print(a[1])
# print("-" * 10)
# for index in range(0, len(a)):
#     print(a[index][0])
# b = [
#     [0, 0],
#     [0, 0]
# ]
# for i in range (len(a)):
#     for j in range (len(a[i])):
#         b[j][i] = a[i][j]
# for i in b:
#     print(i)        #1 task
#range - генерирует список элементов в промежутке от и до
#len - длина object



# b = "1234567890"
# counter = 0
# while True:
#     parol = input("Введите ваш пароль: ")
#     if counter == 3:
#         print("Попробуй в другой раз")
#         break
#     counter += 1
#     if len(parol) < 8:
#         print("Пароль неверный, нужно больше 8 символов")
#     else:
#         k = False  #есть ли в пароле число?
#         for i in b:
#             if i in parol:
#                 k = True
#                 break
#         if k:
#             print("Пароль верный")
#         else:
#             print("Пароль неверный")         #2 task



a = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]
a = [1, 2, 3, 4]
a = [
    [1, 2],
    [3, 4],
    [5, 6],
]#таблица
#a[0][1]
b = [[0, 0], [0, 0], [0, 0]]
#len, range
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])













































