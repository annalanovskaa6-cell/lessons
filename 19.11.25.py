# fantasy_readers = {"Игорь", "Катя", "Лев", "Марина"}
# # detective_readers = {"Никита", "Катя", "Лев", "Ольга"}
# # sci_fi_readers = {"Никита", "Павел", "Лев", "Марина"}
# # two_genres = (
# #         ((fantasy_readers & detective_readers) - sci_fi_readers) |
# #         ((sci_fi_readers & detective_readers) - fantasy_readers) |
# #         ((fantasy_readers & sci_fi_readers) - detective_readers)
# # )
# # print(two_genres)        #4 task hw




# sets = {
#     "key" : "value",
#     "key1" : [
#         1, 2, 3, 4
#     ]
# }   #словарь с элементом {ключь : значение} (dict)
# print(sets["key"])
# print(sets["key1"][2])

# my_dict = [
#     ("ключ1", "значение1"),
#     ("ключ2", "значение2"),
#     ("ключ3", "значение3")
# ]
# print(my_dict, dict(my_dict))

# d = {}   #dict
# d = {1, 2}   #set
# b = {1 : 3, 3 : 5}
# print(b[3])

# d = {"key1" : "value1"}
# print("key1" in d)
# b = [1, 2, 3]
# d["key1"] = 100
# d["key2"] = 1000
# del d["key1"]
# print(d)

# d = {"key1" : "value1", "key2" : "value2"}
# for i in d:
#     print(i, d[i])

# print(list(d.items()))   #получает все элементы словаря как список кортежей
# for i, j in d.items():
#     print(i, j)

# print(list(d.values()))   #возвращает список значений
# print(list(d.keys()))   #список ключей

# print(d.get("key1", 10))   #get(key, value if not exists)
# print(d.pop("key3", 10), d)   #pop - удаляет элемент и возвращает значение

# print(d.popitem())   #удаляет и возвращает последний элемент

# d.update({"key3" : "value3"})   #добавляет элемент
# print(d)

# d.clear()   #очищает словарь

# d = {"key1" : "value1", "key2" : "value2"}
# a = d.copy()   #создаёт копию элемента в памяти
# a["key3"] = "value100"
# print(d, a)

# keys = ["key1", "key2", "key3", "key4"]
# new_dict = dict.fromkeys(keys, 10)
# print(new_dict)

# my_dict = {}
# my_dict.update({'name':'Алиса'})
# print(my_dict)          #1 task



# points = {"x": 10}
# print(points.get("y"), 0)          #2 task



# books = {"романы": 10, "детективы": 5}
# books.update({"фантастика": 8})
# print(books)          #3 task



# marks = {
#     "Информатика": 5,
#     "Математика": 5,
#     "Русский": 3,
#     "История": 4,
#     "Физика": 4}
# print(sum(marks.values()) / len(marks))          #4 task



# keys_values = input("Enter keys and values: ").split(" ")
# s = {}
# for i in keys_values:
#     i.split(":")
#     key, value = i.split(":")
#     s[key] = int(value)
# print(s)          #5 task



# students = ["Анна", 5, "Борис", 4, "Вера", 5]
# f = {}
# for i in range(0, len(students), 2):
#     f[students[i]] = students[i + 1]
# print(f)          #6 task