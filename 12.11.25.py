# a = int(input())
# b = []
# while a:
#     b.append(a % 10)
#     a //= 10
# b.sort()
# print(b)            #hw 1




# a = (1, 2, 3, 4, 5)   #кортеж - tuple()
# b = [1, 2, 3, 4, 5]
# print(tuple(b))   #перевод типов

# DENNIM = "hello world"
# s = ("Hello", "World")

# X = 100
# Y = 300
# coords = (100, 300)
#
# values = (1, 2, 3, 4, 5)
# x = 1
# y = 2
# x, y = y, x
# s1, *s2, s3, s4 = values
# print(s1, s2, s3, s4)

# s = (1, 2, 3)
# s1 = (4, 5)
# print(*s, *s1)
# s3 = (*s, *s1)
# print(s3)

# next_tuple = (1, (2, 3, 4), 5)
# s1, (s2, *s4), s3 = next_tuple
# print(s4)
# print(next_tuple[1][1:])

#s = ((1, 2), (3, 4), (5, 6))
# for i in s:
#     print(i[0], "+", i[1], "=", i[0] + i[1])
# for i, j in s:
#     print(i, "+", j, "=", i + j)

# next = [([1, 2], 3), ["XY", 6]]
# for ((i, b), j) in next:
#     print(i, b, j)      #1 task

#set
# a = {1, 2, 3 ,4, 5, 6, 1, 2, 3 ,4, 5}
# b = [1, 2, 3, 5]
# print(set(b))
# print(a)

# s = {(1, 2), (3, 4)}
#s = {[1,2], [3, 4]}  - error
# print(s)

# s.add((5, 6))   #add - добавление элемента во множество
# print(s)

# s.remove((1, 2))   #remove - удаление элемента множества
# print(s)

# s.clear()
# print(s)

set_1 = {1, 2, 3, 4 ,5, 6}
set_2 = {4 ,5, 6, 7 ,8 ,9}
# set_3 = set_1.union(set_2)   #union - объединение
# set_4 = set_1.update(set_2)
# print(set_3)

# set_3 = set_1.intersection(set_2)   #intersection - пересечение
# set_3 = set_1.symmetric_difference(set_2)   #симметричная разность
# set_1.intersection_update(set_2)

# set_3 = set_1.difference(set_2)   #разность

# set_1 = {1, 2, 3}
# set_2 = {4, 1, 2, 3, 8, 9}
# print(set_2.issubset(set_1))
# print(set_1.issubset(set_2))
#
# print(set_2.issuperset(set_1))
# print(set_1.issuperset(set_2))

# s = (1, 2, 3)
# s1, s2, s3 = s
# print(s1)
# print(s2)
# print(s3)        #2 task



# a = input("Введите ваши числа: ").split(" ")
# for i in range(len(a)):
#     a[i] = float(a[i])
# s = tuple()
# *s, s1 = a
# #reversed .reverse list
# s = reversed(s)
# print(s[::-1], s1)         #3 task



# a = (1, 2, 3)
# b = (4, 5, 6)
# res= ()
# for i in range(len(a)):
#     # res = (*res, a[i] + b[i])
#     res += (a[i] + b[i],)
# print(res)         #4 task



# s = input("Введите строку: ")
# b = set(s)
# print(b, len(b))
# print("yes" if len(b) < len(s) else "no")       #5 task