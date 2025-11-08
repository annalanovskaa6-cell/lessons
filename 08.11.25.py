# a = [1, 2, 10, 1000, 999, 5, 10, 15, 5]
# minimum = 27273747842919283874
# count = 0
# for i in a:
#     if i < minimum:
#         minimum = i
#         count += 1
# print(minimum, count - 1)       #hw 1




# from random import randint
# a = []
# for i in range(5):
#     a.append(randint(1,9))
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)         #1 task



# nums = [1, 2, 3, 4, 5, 6]
# avg = int(sum(nums) / len(nums))
# for i in nums:
#     if i == avg:
#         nums.remove(i)
# print(nums)        #2 task



# a = [1, 99, 23, 102, 78, 52]
# k = []
# for i in range(1, len(a) - 1):
#     if a[i] > a[i + 1] and a[i] > a[i - 1]:
#         k = [a[i],i]
#         break
# print(k[0], k[1])         #3 task



# s = input("Введите список чисел: ").split(" ")
# for i in s:
#     if s.count(i) > 1:
#         for _ in range(s.count(i)):
#             s.remove(i)
# print(s)         #4 task



# s = [2, 4, 2, 9, 8, 3, 4, 2, 1, 9, 3, 2, 8, 5, 9]
# unique = set()
# unique_el = []
# for num in s:
#     if num not in unique:
#         unique.add(num)
#         unique_el.append(num)
# print(len(unique_el), sum(unique_el))        #5 task ver.1

# s = [2, 4, 2, 9, 8, 3, 4, 2, 1, 9, 3, 2, 8, 5, 9]
# maxim = 0
# for i in range(len(s)):
#     seen =[]
#     for j in range(i, len(s)):
#         if s[j] in seen:
#             break
#         seen.append(s[j])
#     if len(seen) > maxim:
#         maxim = len(seen)
#         cash = seen
# print(maxim, sum(cash), cash)        #5 task ver.2