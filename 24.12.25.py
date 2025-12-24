# s = "Hello WORld"
# result = ""
# for i in s:
#     code = ord(i)
#     if 65 <= code <= 90:
#         result += chr(code + 32)   #из кода в значение
#     else:
#         result += i
# print(result)           #hw




# s = "hello world"
# b = "hello"
# print(s.startswith(b))

# def startswith(str1, str2):
#     if str1 < str2:
#         return False
#     else:
#         for i in range(len(str2)):
#             if str2[i] != str1[i]:
#                 return False
#     return True
# print(startswith("hello world", "hello"))                #1 task



# def count(str, substr):
#     count = 0
#     if str < substr:
#         return False
#     else:
#         for i in range(len(str)):
#             flag = False
#             for j in range(len(substr)):
#                 if str[i + j] != substr[j]:
#                     flag = True
#                     break
#             if not flag:
#                 count += 1
#     return count
# print(count("hello world hello python hello", "hello"))         #2 task



# def replace(str, old, new):
#     string = ""
#     if old not in str:
#         return False
#     i = 0
#     while i < len(str):
#         flag = False
#         for j in range(len(old)):
#             if str[i + j] != old[j]:
#                 flag = True
#                 break
#         if not flag:
#             string += new
#             i += len(old)
#         else:
#             string += str[i]
#             i += 1
#     return string
# print(replace("hello hello world", "hello", "world"))              #3 task