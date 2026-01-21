# sign = lambda x: "positive" if x > 0 else "zero" if x == 0 else "negative"
# print(sign(5), sign(-3), sign(0))          #hw 2



# with open('2601.txt', 'r') as file:
#     N = int(file.readline())
#     data = list(map(int, file))
# data = sorted(data, reverse=True)
# print(data)
# res = [data[0]]
# for i in data[1:]:
#     if res[-1] - i >= 9:
#         res.append(i)
# print(len(res), res[-1])           #hw 4



# def calculator(x, y, lambda1, lambda2):
#     a = [
#         lambda1(x, y),
#         lambda2(x, y)
#     ]
#     return a
# print(calculator(
#     10, 4,
#     lambda1=lambda x, y: x + y,
#     lambda2=lambda x, y: x - y
# ))             #hw 3




#MAP
#map(функция, список(итерируемый объект))
#map - метод, который позволяет применить функцию к каждому элементу последовательности

# def plus5(x):
#     return x + 5
# a = [2,3,4,5]
# print(list(map(plus5, a)))
# print(list(map(lambda x: [[]]*x, a)))

# user = [
#     {"username": "daniel", "age": 10},
#     {"username": "daniel1", "age": 15},
#     {"username": "daniel2", "age": 16},
#     {"username": "daniel3", "age": 20},
# ]
# print(list(map(lambda user_item: user_item["username"], user)))       #1 task



#FILTER
# nums = list(range(0, 10))
# nums = ['1', '2', '3']
# evens = list(filter(lambda x: int(x) % 2 == 0, nums))
# print(evens)

# def plus():
#     return "+"
# def minus():
#     return "-"
# def nums(fplus, fminus):
#     return fplus(), fminus()
# s = {
#     "plus": plus
# }
# print(nums(plus, minus))
# print(s["plus"]())

# nums = [1, 2, 3, 4, 5]
# print(list(map(lambda x: x ** 2, nums)))           #2 task



# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(lambda num: num % 2 != 0, nums)))         #3 task



# words = ['apple', 'banana', 'cherry', 'date']
# print(list(map(lambda w: len(w), words)))           #4 task



# nums = [-5, -2, 0, 3, 7, -1, 10]
# print(list(filter(lambda num: num > 0, nums)))             #5 task



# a = [1,1,1,1,1,1]
# b = [2,2,2,2,2,2]
# print(list(map(lambda x,y: x + y, a, b)))
# c = [3,3,3,3,3,3] - конечный список

# list1= [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# print(list(map(lambda x,y: x * y, list1, list2)))           #6 task

# def is_simple(x):
#     if 0 <= x <= 2:
#         return False
#     for i in range(2,int(x / 2) + 1):
#         if x % i == 0:
#             return True
#     return False
# nums = [2,3,4,5,6,7,8,9,10,11,12]
# print(list(filter(is_simple, nums)))            #7 task



# def my_map(func, iterable):
#     result = []
#     for item in iterable:
#         result.append(func(item))
#     return result
# nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(my_map(lambda x: x * 2, nums))               #8 task