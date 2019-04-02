# def fn():
#     print("fn...")
#
#
# my = fn  # shallow copy
# print(id(my), id(fn))  # memory address
# print(id(my) == id(fn))  # memory address
# my()


def fn():
    print('fn...')


def fn1():
    print('fn1...')


def defaultFn():
    print('etc')


d = {1: fn, 2: fn1}
d.get(3, defaultFn)()
