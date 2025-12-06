# from random import randint
# d = {"A": 10, "B": 20, "C": 30}
# c = {}
# c.update({
#     randint(100, 999): d["A"],
#     randint(100, 999): d["B"],
#     randint(100, 999): d["C"]
# })
# with open ("test.txt", "w+") as file:
#     for key, value in c.items():
#         file.write(str(key) + ": " + str(value) + "\n")
# with open ("test.txt", "r") as file:
#     for item in file.readlines():
#         print(item)          #hw 2



# from random import randint
# with open ("test.txt", "w") as file:
#     for i in range(50):
#         file.write(str(randint(1, 100)) + "\n")
# with open ("test.txt", "a") as file:
#     for i in range(20):
#         file.write(str(randint(1, 100)) + "\n")
# with open ("test.txt", "r") as file:
#     a = file.readlines()
#     summ = 0
#     for i in a:
#         summ += int(i)
#     print(summ)          #hw 3




# import string
# print(string.punctuation)
# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

# print("hello" + ":" + "world")
# sign = ":"
# print(f"hello{sign}world")



# from random import randint, choice
# import string
# list_pairs = []
# for i in range(100):
#     a = choice(string.ascii_uppercase)
#     a += f"{randint(0, 9)}\n"
#     list_pairs.append(a)
# with open("test.txt", "w") as file:
#     file.writelines(list_pairs)
# with open("test.txt", "r") as file:
#     for i in file:
#         if int(i[1]) % 2 == 0 and i[1] != "0":
#             print(i)
#             break
# with open("test.txt", "r") as file:
#     count = 0
#     for i in file:
#         if i[0] == "A":
#             count += 1
#     print(count)          #1 task



# from random import randint, choice
# import string
# list_pairs = []
# for i in range(150):
#     a = choice(string.ascii_uppercase)
#     a += f"-{randint(0, 9)}\n"
#     list_pairs.append(a)
# with open("test.txt", "w") as file:
#     file.writelines(list_pairs)
# with open ("test.txt", "r") as file:
#     for i in file:
#         if int(i[2]) > 5:
#             print(i)          #2 task



# with open ("903.txt", "r") as file:
#     s = []
#     for line in file:
#         numbers = line.split("\t")
#         maxim = 0
#         minim = 9999999
#         for i in numbers:
#             s.append(int(i))
#             if int(i) > maxim:
#                 maxim = int(i)