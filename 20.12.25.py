# a = input()
# b = int(a, 16)
# binar = bin(b)[2:]
# print(binar)
# print(binar.count('1'))          #8 task



# a = input()
# summ = 0
# for i in a:
#     summ += int(i)
# print(summ)              #9 task



# a = input()
# b = a.split(",")
# print(b[0].find(b[1].strip()))
# print(b[0][10:-6])
# print(b[0][::-3])             #10 task



# b = input()
# a = b.split(",")
# for i in a:
#     print(i.strip())
# s = ""
# for i in b:
#     if i.isdigit():
#         s += i
# print(s)                #12 task



# a = list(map(int, input().split()))
# b = []
# for i in a:
#     if i % 2 != 0:
#         a.remove(i)
# print(sum(a))              #14 task



# a = map(int, input().split(" "))
# b = []
# s = False
# for i in a:
#     if not(i % 2 == 0 and i % 13 == 0):
#         b.append(i)
#     else:
#         s = True
#         break
# if not s:
#     print("Нет подходящих чисел")
# else:
#     print(sum(b))                #13 task



# numbers = list(map(int, input().split(" ")))
# print(numbers[::2])
# print(numbers.index(min(numbers)))
# numbers.remove(max(numbers))
# print(numbers)
# print(sorted(numbers, reverse=True))             #15 task



# list_1 = [1, 2, 3, 4, 2, 3, 4, 6, 8]
# list_2 = list(map(int, input().split(" ")))
# print(tuple(set(list_1) & (set(list_2))))              #task



#ASCII - таблица
# print(ord("H"))
# print(chr(72))