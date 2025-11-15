# t = (1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 6, 6)
# count = 0
# maximum = 0
# for i in range(1, len(t)):
#     if t[i] == t[i - 1]:
#         count += 1
#     else:
#         if maximum < count:
#             maximum = count
#         count = 1
# print(maximum)          #1 task



# cart = [("яблоки", 100), ("хлеб", 50), ("молоко", 80), ("яблоки", 100)]
# name = []
# for n, p in cart:
#     if p > 70:
#         name.append(n)
# prices = []
# for n, p in cart:
#     prices.append(p * 2)
# view = set()
# unique = []
# for n, p in cart:
#     if n not in view:
#         view.add(n)
#         unique.append((n, p / 2))
# print(name)
# print(prices)
# print(unique)          #2 task



# books = [("Война и мир", 1865), ("1984", 1949), ("Гарри Поттер", 1997), ("Война и мир", 1865)]
# year = []
# for i, j in books:
#     if j > 1900:
#         year.append(i)
# years = []
# for i, j in books:
#     years.append(j - 100)
# new = []
# for i, j in books:
#     if j < 1950:
#         title = "Классика: " + str(i)
#         new.append(title)
# print(year)
# print(years)
# print(new)          #3 task



# math_students = {"Анна", "Борис", "Вера", "Глеб"}
# physics_students = {"Борис", "Вера", "Дмитрий", "Елена"}
# chemistry_students = {"Вера", "Глеб", "Дмитрий", "Жанна"}
# set_1 = math_students.intersection(physics_students, chemistry_students)
# set_2 = math_students.difference(physics_students, chemistry_students)
# set_3 = math_students.union(physics_students) - chemistry_students
# print(set_1)
# print(set_2)
# print(set_3)          #4 task



# even = set(range(2,21,2))
# multi = set(range(3, 31, 3))
# intersection = even.intersection(multi)
# both = {i for i in range(1,21) if i % 2 == 0 and i % 3 == 0}
# print(even)
# print(multi)
# print(intersection)
# print(both)          #5 task ver.1

# a = set()
# for i in range(2, 21, 2):
#     a.add(i)
# a1 = set()
# for i in range(0, 28, 3):
#     a1.add(i)
# a2 = set()
# for i in range(1, 21):
#     if i % 2 == 0 and i % 3 == 0:
#         a2.add(i)
# print(a)
# print(a1)
# print(a.intersection(a1))
# print(a2)          #5 task ver.2