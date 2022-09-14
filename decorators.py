# user = "admin"
#
#
# def post_article(text: str) -> None:
#     if user == "admin":
#         print(f"Article '{text}' was posted")
#     else:
#         print("you must be admin")
#
#
# post_article("dobriyden`")
# post_article('sdljkg.dlmjkknznmkljnvjkhsdfml;sdgkfjnndsfg')


# import time
#
#
# def timer(func):
#     def inner(*args):
#         start_time = time.time()
#         res = func(*args)
#         end_time = time.time()
#         print(f"Time was:{end_time - start_time:.2f}")
#         return res
#
#     return inner
#
#
# def decorate(func):
#     def inner(*args):
#         print("start function")
#         func(*args)
#         print("end_function")
#     return inner
#
#
# @decorate
# @timer
# def very_slow_func():
#     i = 0
#     for _ in range(400000):
#         i += 3
#     return i
#
#
# @decorate
# @timer
# def long_function(num):
#     return sum(range(num))

#
# very_slow_func()
# long_function(9000000)

# def make_multiply_of(x: int):
#     def multiply(num: int):
#         return x * num
#     return multiply
#
#
# c = make_multiply_of(3)
# print(c(5))


# def decorate(func):
#     def inner():
#         print("decorator before")
#         func()
#         print("decorator after")
#     return inner

#
# @decorate
# def printer():
#     print("hello,mates")
#
#
# printer()

# import time
#
#
# def delay(seconds: int):
#     def inner(func):
#         def wrapper(*args, **kwargs):
#             print(f"Sleeping {seconds} sec")
#             for i in range(seconds):
#                 time.sleep(1)
#                 print(i+1)
#             return func(*args, **kwargs)
#
#         return wrapper
#     return inner
#
#
# @delay(10)
# def printer(name: str):
#     print(f"Hello, {name}!")
#
#
# printer("Sergiy")
#
# import time
#
#
# def timer(func):
#     def inner(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         end = time.time()
#         print(f"Time was {end - start} sec")
#         return res
#
#     return inner
#
#
# @timer
# def add(a: int = 0, b: int = 0) -> int:
#     """
#     This functoin returns something
#     :param a:first param(defolt = 0)
#     :param b: second param(defolt = 0)
#     :return: sum of them
#     """
#     return a + b
#
#
# help(add)
