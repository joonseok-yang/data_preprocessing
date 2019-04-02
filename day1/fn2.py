#일급함수
# 함수에 대해 return, 인자, 할당

def fn():
    print('fn...')

def fn1():
    print('fn1...')

d={1:fn, 2:fn1}
d[1]()
# my = fn #shallow copy
# print( id(my), id(fn) )
# my()
