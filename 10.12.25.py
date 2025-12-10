# with open("902.txt", "r") as file:
#     counter = 0
#     for line in file:
#         s = line.split()
#         d = []
#         for i in s:
#             d.append(int(i))
#         d = sorted(d)
#         counter_amount = 0
#         for i in range(len(d)):
#             counter_cash = -1
#             for j in range(len(d)):
#                 if d[i] == d[j]:
#                     counter_cash += 1
#             if counter_cash > 1:
#                 counter_amount += 1
#         if d[-1] > sum(d[:-1]) and counter_amount == 0:
#             counter += 1
#     print(counter)               #hw 1



# with open ("903.txt", "r") as file:
#     counter = 0
#     for line in file:
#         numbers = line.split("\t")
#         s = []
#         for i in numbers:
#             s.append(int(i))
#         s = sorted(s)
#         sum_rst = sum(s[1:-1]) >= (s[0] + s[-1])
#         if sum_rst:
#             counter += 1
#     print(counter)            #hw 2




# with open("900.txt", "r") as file:
#     amount_lines = 0
#     for line in file:
#         numbers = line.split("\t")
#         s = []
#         for i in numbers:
#             s.append(int(i))
#         counter = 0
#         first = []
#         second = []
#         for i in s:
#             if s.count(i) != 1:
#                 first.append(i)
#                 continue
#             second.append(i)
#         if len(set(s)) == 4 and sum(first) ** 2 >= sum(second) ** 2:
#             amount_lines += 1
#     print(amount_lines)             #1 task



# with open("905.txt","r") as file:
#     amount_lines = 0
#     for line in file:
#         numbers = line.split("\t")
#         s = []
#         for i in numbers:
#             s.append(int(i))
#         if len(set(s)) == 3 and s.count(max(s)) == 3:
#             amount_lines += 1
#     print(amount_lines)               #2 task