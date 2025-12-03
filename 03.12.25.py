# s = "0123456789"
# def words(text, **options):
#    if options.get("ignore_case", False):
#        text = text.lower()
#    if options.get("ignore_nums", False):
#        for i in s:
#            text = text.replace(i, "")
#    text_list = text.split()
#    text_set = set(text_list)
#    dict_new = {}
#    for text_set_item in text_set:
#        dict_new[text_set_item] = text_list.count(text_set_item)
#    return dict_new
# print(words("hello23 World HeLLo", ignore_case=True, ignore_nums=True))       #hw 2




#открытие файла маршрут/ режим открытия/ кодировка при чтении
# file = open("test.txt", "r", encoding="utf-8")
#"r" - чтение
#"w" - запись
#"a" - добавлять в конец файла(от слова append)
#"x" - открывает файл для записи, только если он не существует
#rb, wb, ab, xb - бинарные действия
#r+/x+ - открывает файл для чтения и записи (файл должен существовать)
#w+/a+ - открывает файл для записи, если файла нет он его создаст

# print(file.read())   #считывает все строки текстового файла
# print(file.readline())   #считывает одну строку из файла
# print(file.readlines())   #считывает файл как список строк

# print(file.readline())   #курсор в начале первой строки
# print(file.readline())   #курсор в начале второй строки
# print(file.readline())   #курсор в начале третьей строки
# print(file.readline())   #курсор в начале четвёртой строки

# print(file.read(10))
# print(file.tell())   #позиция указателя
# file.seek(0)
# print(file.read(10))

# file.close()   #закрытие файла

#контекстный менеджер
# with open("test.txt", "r", encoding="utf-8") as file:
    # file_item = file.readline()
    # while file_item:
    #     print(len(file_item)-1)
    #     file_item = file.readline()
    # for file_item in file:
    #     print(len(file_item))

# with open("test.txt", "w", encoding="utf-8") as file:
#     file.write("hello world")
#
# with open("test.txt", "a", encoding="utf-8") as file:
#     file.write("\nhello world")
#
# with open("tester.txt", "x", encoding="utf-8") as file:
#     file.write("\nhello world")

# with open("test.txt", "w+", encoding="utf-8") as file:
#     file.write("hello world")
#
# with open("test.txt", "r+", encoding="utf-8") as file:
#     file.write("hello world")

# s = ["hello\n", "world"]
# with open("test2.txt", "w+", encoding="utf-8") as file:
#     file.writelines(s)



# s = ["hello", "world", "hello"]
# with open("test.txt","w+", encoding="utf-8" ) as file:
#     file.writelines(s)
# with open("test.txt","r", encoding="utf-8" ) as file:
#     print(file.read())          #1 task