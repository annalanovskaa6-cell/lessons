#Переменная - именновая ячейка в памяти
test = 10
user_name = "Алиса" #строковый тип - String (str)
max_value = 100 #численный тип - Integer (int)
our_float = 1.6 #число с плавающей точкой  (float)
logical = True #True/False (1 или 0) - Boolean (bool)

#id() - возвращает адрес в памяти
#print(id(user_name), id(max_value), our_float, logical)

a = 2
b = 25443242542
a = b
#print(id(a), id(b))

#type - определяет тип переменной
a = True
#print(type(a))

a = int(1) #переводит в int
#print(type(a), a)
a = float(a) #переводит в float
#print(type(a), a)
a = str(a) #переводит в строку
#print(type(a), a)
a = bool(a) #переводит в bool (логический тип)
#print(type(a), a)

name = "Тотя" #1 task
#print(name)

age = 228 #2 task
#print("Мне", age, "лет")

a = "Текст"
#a - имя, a[index: int]
#index начинаетс с 0; начинается  целого числа
#print(a[0]) #[] - синтаксис получения элемента по индексу

my_list = [1, 2, "hello", 4, 5] #тип данных (list)
#print(my_list[2].__sizeof__()) #показывает размер в битах

my_list = [1,2,3,4,5,6,7,8,9,10] #нет массивов, только list
#*, /, +, - (базовые операторы)
#print(my_list[1] / 3 - 2)

#{} - dictionary (словарь) в качестве аргументов ключ:значение
dictionary = {"a": "икотя"}
#print(dictionary["a"])

#input - команда ввода данных
#a = int(input("Введите число: "))
#print(a * 10)

a = int(input("Число первое: "))
b = int(input("Число второе: "))
print(a + b)


