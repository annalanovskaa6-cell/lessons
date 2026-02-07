# import sys
# sys.setrecursionlimit(100000)
# def hanoi(n, sourse, target, auxiliary, moves = []):
#     if n == 1:
#         moves.append(f"Переместить диск 1 с {sourse} на {target}")
#         return moves
#     hanoi(n - 1, sourse, auxiliary, target, moves)
#     moves.append(f"Переместить диск {n} с {sourse} на {target}")
#     hanoi(n - 1, auxiliary, target, sourse, moves)
#     return moves
# moves_l = hanoi(3, "A", "C", "B")
# for move in moves_l:
#     print(move)
# print(f"Всего ходов {len(moves_l)}")                           #hw
import asyncio

from pip._internal.utils import urls


#АСИНХРОННОСТЬ
# def a():
#     print("hello")
# a()
# print("world")
#процессы (ресурсы / память / файлы / соединения)
#потоки -> (ресурсы от процесса / быстрее создаются и переключаются / могут обмениваться данными)

#Важность процессов ->
#сварить макароны - пожарить мясо
#варить макароны 4мин
#пожарить мясо 4мин
#8 мин

#варить макароны - 2мин
#пожарить мясо в течение макарон -> (3мин)

#ПАРАЛЛЕЛИЗМ
#2мин -> ядра процессов


# import asyncio
# # async with, async for
# async def f():
#     print("Привет")
#     await asyncio.sleep(1)
#     print("Мир")
# asyncio.run(f())

# def sync_f():
#     return "Результат"
# async def async_f():
#     data = [1, 2, 3]
#     print(sum(data))
#     await asyncio.sleep(1)
#     return "Результат"
# print(sync_f())
# print(async_f())
# asyncio.run(async_f())



# async def one(num):
#     print("f_1 start")
#     await asyncio.sleep(num)
#     print("f_1 end")
# async def two(num):
#     print("f_2 start")
#     await asyncio.sleep(num)
#     print("f_2 end")
# async def main():
#     results = await asyncio.gather(one(10), two(1))
#     print(results)
    # task1 = asyncio.create_task(one())
    # task2 = asyncio.create_task(two())
    # while True:
    #     await asyncio.sleep(1)
    #     task1.cancel()
    #     if task2.done():
    #         print("hello")
    # result1 = await task1
    # result2 = await task2
# asyncio.run(main())


# async def download_page(url):
#     print(f"Загружаю {url}")
#     await asyncio.sleep(1)
#     return f"содержимое {url}"
# async def main():
#     urls = [
#         "https://www.python.org",
#         "https://www.python.org/about/",
#         "https://www.python.org/about3/",
#         "https://www.python.org/about9/",
#         "https://www.python.org/about10/",
#         "https://www.python.org/about22/",
#         "https://www.python.org/about300/",
#     ]
#     # TASK = asyncio.create_task(download_page(urls[0]))
#     # await asyncio.gather(TASK)
#     pages = await asyncio.gather(*[download_page(url) for url in urls])
#     print(f"загружено {len(pages)} страниц")
#     for content in pages:
#         print(content)
# asyncio.run(main())

# async def make_coffee():
#     print('Making coffee')
#     await asyncio.sleep(2)
#     print('Coffee is ready!')
# async def make_toast():
#     print('Making toast')
#     await asyncio.sleep(2)
#     print('Toast is ready!')
# from time import time
# time()
# async def main():
#     start = time()
#     await make_coffee()
#     await make_toast()
#     print(time() - start)
# asyncio.run(main())