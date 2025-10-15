#тернарный оператор - действие if условие else действие

#пока условие
#бесконечный цикл если True
# while True: #while условие, например: (a > 10)
#     print("Hello")


#for переменная in итерируемый объект
#list - итерируемый объект
#1 : 1
#3 : 3
#2 : 2
#string - итерируемый объект
#a = "dddfd"
#print(a[0])
#в переменную i записываются элементы посимвольно для каждой итерации цикла

# for i in [1, 2, 3, 4]:
#     print(i)

#range(начало, конец, шаг)
#генерирует список (генератор) чисел от начало до конца - 1
# print(list(range(0, 10)))
# print(list(range(0, 10, 3)))
# print(list(range(10, 0, -1)))

# for i in range(10):
#     print(i)

#break - останавливает выполнение цикла
#continue - останавливает итерацию цикла
# counter = 0
# counter_false = 0
# while True:
#     counter += 1
#     if counter >= 100:
#         break
#     if counter % 3 ==0:
#         counter_false += 1
#         continue
#     print("Наше значение: ", counter)
#
# print("Это количество не кратных: ", counter_false)

# a = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
# for i in a:
#     for j in i:
#         print(j)

# a = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
# i = 0
# j = 0
#len() - возвращает длину object
# print(len(a))
# print(len(a[0]))
#print(a[len(a)-1])

#a = [1, 2, 3]
#отрицательный индекс получает элемент с обратной стороны
#print(a[-2])



# for i in range(11):
#     print(i)      #1 task

# n = int(input())
# for i in range(1, n):
#     print(i ** 2)     #2 task

num = int(input())
for i in range(1, 21):
    if num % 3 == 0:
        break
print("Готово")      #3 task
















