# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# filtered_matrix = list(map(lambda row: list(filter(lambda x: x % 2 == 0, row)), matrix))
# print(filtered_matrix)
# print(list(map(sum, filtered_matrix)))              #hw 4



# def my_filter(func, iterable):
#     a = []
#     for item in iterable:
#         if func(item):
#             a.append(item)
#     return a
# print(my_filter(lambda x: x % 2 == 1, [1, 2, 3]))             #hw 1




# def a():
#     def b():
#         print("Hello World")
#     b()

# def a(text):
#     def b(t):
#         print(t + text)
#     return b("hello")
# a("world")

# def a(name, func):
#     print(name)
# a("boris", lambda x: x * 2)

# def create_discount(category, discount):
#     def bronze(price):
#         return price * 2 - (discount / 100)
#     def silver(price):
#         return price * 0.5
#     def gold(price):
#         return price * 0.1
#     if category == 'bronze':
#         return bronze
#     elif category == 'silver':
#         return silver
#     elif category == 'gold':
#         return gold
# bronze_discount = create_discount('bronze')
# product_price = 1000
# print(f"{bronze_discount(product_price)}")

# def count_10_times(nums):
#     if nums >= 10:
#         return nums
#     return count_10_times(nums + 1)
# print(count_10_times(1))

# name = "hello"
# def a():
#     global name
#     name2 = "world"
#     def next():
#         nonlocal name2
#         name2 = "123"
#     next()
#     print(name2)
# a()

# def create_adder(number):
#     count = 0
#     def add_to():
#         nonlocal count
#         count += 1
#         return count
#     return add_to
# add_one = create_adder(5)   #замыкание
# print(add_one())
# print(add_one())
# print(add_one())

# def make_even_generator(start):
#     def next_even():
#         nonlocal start
#         result = start
#         start = start + 2
#         return result
#     return next_even
# even_gen = make_even_generator(6)
# print(even_gen())
# print(even_gen())
# print(even_gen())
# print(even_gen())
# print(even_gen())               #1 task



# def make_string_builder(string):
#     def string_builder():
#         nonlocal string
#         result = string
#         string += " " + string
#         return result
#     return string_builder
# string_build = make_string_builder("hello")
# print(string_build())
# print(string_build())
# print(string_build())               #2 task



# def make_product_accumulator(start):
#     def product_accumulator(t):
#         nonlocal start
#         start *= t
#         return start
#     return product_accumulator
# make_product = make_product_accumulator(1)
# print(make_product(5))
# print(make_product(3))
# print(make_product(1))
# print(make_product(10))                 #3 task



# def make_counter(start, step):
#     def counter():
#         nonlocal start
#         start += step
#         return start
#     return counter
# next = make_counter(1, 2)
# print(next())
# print(next())
# print(next())              #4 task



# def create_length_filter(min_length):
#     def length_filter(word):
#         return len(word) >= min_length
#     return length_filter
# a = create_length_filter(5)
# print(a("hello"))          #5 task