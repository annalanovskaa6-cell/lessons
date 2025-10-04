#кортеж - набор неизменяемых данных (tuple)
a = (1, 2, 3, 4, 5, 6, 6)
#print(a, type(a))

#set - набор упорядочных по возрастнию уникальных значений (неизменяемых)

a = {1, 2, 3, 4, 5, 5}
#print(a, type(a))

list_1 = [1, 2, 2, 2, 2, 4, 4, 4, 6, 6, 6, 6]
#print(set(list_1))
#{1, 2, 4, 6} тип данных set

a = ["раз", "два", "три"]
#print(a[0], a[1], a[2], sep = "-")

dictionary = {"Имя": "Иван", "Фамилия": "Иванов", "Возраст": 17, "Класс": "11A"}
#print(dictionary["Имя"],dictionary["Фамилия"],dictionary["Возраст"],dictionary["Класс"]) #1 task


a = 45
a = str(a)
#print("Число в строке : 45")    #2 task


a = ["one", "two", "three"]
#print(a[0], a[1], a[2], sep = ",")    #3 task


#a = input("Number 1: ")
#b = input("Number 2: ")
#a = int(a)
#b = int(b)
#print(a + b)      #4 task


#a, b, c = input(),input(),input()
#print(a,b,c,sep=":")    #5 task


#split - разделяет строку по разделителю
#a = input().split(' ')
#print(a[0], a[1], a[2], a[3], sep=':')


#a = "Python"
#a = list(a)
#print(a)      #6 task


my_tuple1 = (1, 2, 3, 4)
my_tuple2 = list(my_tuple1)
#print(id(my_tuple1), id(my_tuple2), sep = ";")    #7 task

a = (1, 2, 3, 4)
b = [1, 2, 3, 4]
b[0] = 5
#print(a)
#print(b)



