# from random import randint
# a = [
#     randint(1, 100),
#     randint(1, 100),
#     randint(1, 100),
#     randint(1, 100),
#     randint(1, 100)
# ]
# maxim = 0
# minim = 100000
# for i in a:
#     if maxim < i:
#         maxim = i
#     if minim > i:
#         minim = i
# print(maxim, minim)          #hw 1

# s = input().strip(" ")
# count = 0
# len_s = len(s)
# for i in range(len_s):
#     for j in range(i + 1, len_s):
#         if s[i] == s[j] and j - i > 1:
#             count += 1
# print(count)       #hw 3




# a = [1, 2, 3]
# iterator = iter(a)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
# for i in a:
#     print(i)

# k = [1, 2, 3]
# k = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in range(0, len(k)):
#     k[i] += 1
# print(k)

# k = [1, 2, 3]
# l = [4, 5, 6]
# z = k + l
# k.extend(l)   #extend - расширяет один объект другим
# print(k)

# from random import randint
# k = []
# for i in range(5):
#     #append - добавляет новый элемент в конец списка
#     k.append(randint(0, 100))
# print(k)

# k = ["Раз", "Три"]
# j = "Два"
# k.insert(1, j)   #insert - вставляет перед необходимым индексом значение
# print(k)

# k = [1, 2, 3, 4, 2, 5]
# k.remove(3)   #remove - удаляет первый найденный элемент
# print(k)

# k = [1, 2, 3, 4, 2, 5]
# k.clear()
# print(k)   #clear - чистит список

# k = [1, 2, 3, 4, 2, 5]
# k.pop(4)   #pop - удаляет элемент по индексу
# print(k)

# k = [5, 4, 3, 2, 1]
# k = ["alfa", "celcy", "beta"]
# k.sort(reverse = True)
# print(k)

# k = [1, 2, 3, 4, 5]
# k.reverse()   #reverse -
# print(k)

# k = [1, 2, 3, 4, 5]
# print(max(k))
# print(min(k))
# print(len(k))




# k = [1, 2, 3, 4, 5]
# for i in range(0, len(k)):
#     k[i] = k[i] * 2
# print(k)      #1 task



# k = [1, 2, 3, 4, 5]
# iterator = iter(k)
# summ = 0
# for _ in range(len(k)):
#     summ += next(iterator)
# print(summ)      #2 task



# k = [1, 2, 3]
# l = [4, 5, 6]
# for i in range(len(l)):
#     print(l[i] + k[i], end = " ")       #3 task



# k = ["arr", "brbr", "patapim", "skrrrr"]
# for x in k:
#     count = 0
#     for _ in x:
#         count += 1
#     if count % 2 == 0:
#         print(x)        #4 task



# from random import randint
# for _ in str(randint(0, 100000)):print("Разряд")      #5 task