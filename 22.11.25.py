# s1 = input().split()
# s2 = input().split()
# set_s1 = set(s1)
# set_s2 = set(s2)
# dict_1 = dict.fromkeys(set_s1, 0)
# dict_2 = dict.fromkeys(set_s2, 0)
# for i in s1:
#     dict_1[i] += 1
# for i in s2:
#     dict_2[i] += 1
# for key, value in dict_1.items():
#     if key not in dict_2:
#         dict_2[key] = value
#     else:
#         dict_2[key] += value
# print(dict_1)
# print(dict_2)          #1 task



# a = sorted(input().split())
# dict_a = dict.fromkeys(a, 0)
# dict_b = {}
# for i in dict_a.keys():
#     dict_a[i] = a.count(i)
#     if dict_a[i] > 1:
#         dict_b.update({i: dict_a[i]})
# print(dict_a)
# print(dict_b)          #2 task



# students = [
#     {'name': 'Alice', 'group': 'A', 'score': 85},
#     {'name': 'Bob', 'group': 'B', 'score': 92},
#     {'name': 'Charlie', 'group': 'A', 'score': 78},
#     {'name': 'David', 'group': 'C', 'score': 88},
#     {'name': 'Eve', 'group': 'B', 'score': 95}
# ]
# s = {}
# for student in students:
#     if student['group'] in s:
#         s[student['group']].append(student['name'])
#     else:
#         s[student['group']] = [student['name']]
# print(s)         #3 task


# a = input().replace(" ", "")
# b = {}
# for i in a:
#     b[i] = a.count(i)
# s = [["", 0], ["", 0], ["", 0]]
# for i in b:
#     for j in range(len(s)):
#         if s[j][1] < b[i]:
#             s[j][0] = i
#             s[j][1] = b[i]
# print(b)         #4 task