# def make_stats_tracker():
#     numbers = []
#     total = 0
#     def add(value):
#         nonlocal total
#         numbers.append(value)
#         # total += value
#         print(f"Добавлен новый элемент: {value}")
#     def avg():
#         return sum(numbers) / len(numbers)
#     def maxim():
#         return max(numbers)
#     def minim():
#         return min(numbers)
#     def get_stats():
#         dict_test = {
#             "max": maxim(),
#             "min": minim(),
#             "avg": avg(),
#             "numbers": numbers
#         }
#         return dict_test
#     return add, get_stats
# add_value, getstats = make_stats_tracker()
# add_value(2)
# add_value(3)
# add_value(4)
# print(getstats())                     #hw 1



# def apply_to_each(fnumbers, operation):
#     result = []
#     for num in fnumbers:
#         processed = operation(num)
#         result.append(processed)
#     return result
# def square(number):
#     return number ** 2
# numbers = [1, 2, 3]
# square_result = apply_to_each(numbers, square)
# print(square_result)               #hw 3




#с логом
# def add_with_logging(a, b):
#     result = add(a, b)
#     print(f"Выполнилась функция add: {a} + {b} = {a + b}")
#     return result
#
# def mul_with_logging(a, b):
#     result = mul(a, b)
#     print(f"Выполнилась функция mul: {a} * {b} = {a * b}")
#     return result

# def create_logging_wrapper(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f"Вызвана функция {func.__name__} с аргументом {args}, результат: {result}")
#         return result
#     return wrapper
# @create_logging_wrapper
# def add(a, b):
#     return a + b
# @create_logging_wrapper
# def mul(a, b):
#     return a * b
# print(add(2, 3))
# add_with_logging = create_logging_wrapper(add)
# mul_with_logging = create_logging_wrapper(mul)
# print(add_with_logging(1, 2))
# print(mul_with_logging(1, 2))


# import time
# start = time.time()
# a = 1 + 1
# end = time.time()
# print(end - start)
# start = time.time()
# for i in range(10000):
#     pass
# end = time.time()
# print(end - start)


# from time import time
# def timeit_func(func):
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = func(args)
#         print(time() - start)
#         return result
#     return wrapper
# @timeit_func
# def add(nums = []):
#     summ = 0
#     for num in nums:
#         summ += num
#     return summ
# @timeit_func
# def mul(nums = []):
#     mull = 1
#     for num in nums:
#         mull *= num
#     return mull

# from time import time
# def parent(func):
#     def wrapper(*args, **kwargs):
#         start = time()
#         a = func(*args)
#         print(time() - start)
#         return a
#     return wrapper
# @parent
# def test(tfunc, list_nums):
#     for i, num in enumerate(list_nums):
#         list_nums[i] = tfunc(num)
#     return list_nums
# a = test(lambda x: x ** 3, [1,2,3])
# print(a)