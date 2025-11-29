# a = ("heLlo")
# b = ""
# for i in range(len(a)):
#     if a[i].isupper():
#         b += "_" + a[i]
#     else:
#         b += a[i]
# print(b.lower())




# def analyze_text(text):
#     count = len(text)
#     words = text.split(" ")
#     word_count = len(words)
#     sentences  = text.count(".") + text.count("!") + text.count("?")
#     return (count, word_count, sentences)
# text = input("Enter a text: ")
# print(analyze_text(text))          #1 task



# def calculate_area(shape='rectangle', length=0, width=0, radius=0):
#     if shape == 'rectangle':
#         return length * width
#     elif shape == 'circle':
#         return 3.14 * (radius ** 2)
# length = 12
# width = 19
# radius = 5
# print(calculate_area(shape='rectangle', length=length, width=width, radius=radius))       #2 task



# def format_name(first, last, middle="", title=""):
#     return title + " " + first + " " + last + " " + middle
# print(format_name("John", "Smith", title = "Mr"))          #3 task



# def values(*args):
#     unique = set(args)
#     return list(unique)
# print(values(1,2,2,3,4,5,6,6,5,4))           #4 task



# from random import randint
# def f_nums(a:int, b:int):
#     list_nums = []
#     for _ in range(a, b):
#         z = randint(1, 100)
#         list_nums.append(z)
#     maxim = 0
#     digit = -1
#     for i in list_nums:
#         value_cash = list_nums.count(i)
#         if maxim < value_cash:
#             digit = i
#             maxim = value_cash
#     return list_nums, digit, maxim
# print(f_nums(1, 50))           #5 task