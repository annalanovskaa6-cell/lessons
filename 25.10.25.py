# H = int(input())
# counter = 0
# for i in range(1, H * 2, 2):
#     counter += 1
#     print(" " * (H - counter), end="")
#     for j in range(1, counter):
#         print(j, end=" ")
#     for j in range(counter, 0, -1):
#             print(j, end=" ")
#     print()         #hw 5




# a = "abcdABCD"
# for i in a:
#     print(ord(i), i)
# print("q" < "w")

# a = "10"
# print(int(str(a), 16))

# print("\n\t")
# print('\'')
# print("\U0001F600")
# g = r"https:\\google.com"
# print(g)

# name = "Миша"
#s[n : m : k]
#n - начало среза
#m - конец среза (не включительно)
#k - шаг среза
# print(name[0 : 4 : 2])   #Мш
# print(name[-1])
# print(name[::-1])

string = "   heТДO woKLN   "

print(string.find("d"))  #поиск первого вхождения подстроки
# print(string.index("dffr")) #возвращает индекс подстроки, если такого нет выведет ошибку
# print(string.rfind("w"))
print(string.split(" ")) #делит строку по разделителю " "
print(string.count(" ")) #считает количество подстрок
print(string.lower()) #делает текст в нижнем регистре
print(string.upper()) #поднимает текст с колен (верхний регистр)
print(string.isdigit()) #все символы строки это числа
string = "hello "
print(string.isalpha()) #True, если нет пробелов и цифр
print(string.isalnum()) #два верхних метода в одном
string = "***hello world***"
print(string.strip("*")) #удаляет выбранный символ в начале и конце строки (по умолчанию - пробел)
#replace(символ, на что меняем, сколько раз)
print(string.replace("*", "#", 2))
l = ["h", "e", "l", "l", "o"]
print("".join(l)) #соединяет элементы с разделителем

# string = "abayunda"
# print(string[-4:])      #1 task



string = input()
print(string[0 : -1 : 2])      #2 task





















