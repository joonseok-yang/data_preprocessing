def fn():
    print('hello')
    print('korea')

def hap(a,b):
    return a+b

def fn1():
    return 10,20

def shape(r,h,w):
    return r**2*3.14, h*w

def fn2(a,b):
    print(a,b)

def fn3(a=10,b=20,c=30):
    print(a,b,c)

def fn4( *args ):
    print(args)

def fn5(a):
    print(a)

def circles(*rs):
    for r in rs:
        print(r**2*3.14)

def fn6(**kwargs):
    print(kwargs)

fn6( aa=10,bb=20)
fn6(name='홍길동',age=20)

# circles(1,2,3,4,5)
# fn4(10,20,30)`
# fn4("aa","bb")
# fn5(10)
# fn5('abc')
# fn5([1,2,3])


# print(10,20,sep='-')
# print('hello',end=' ')
# print('python')

# fn3()
# fn3(100)
# fn3(100,200)
# fn3(100,200,300)
# fn3(b=1000)



# fn2(b=1000,a=2000)
# fn2(100,200)

# rst = shape(3,10,20)
# print(rst)
# rst = fn1()
# print(rst)
# a,b = fn1()
# print(a,b)


# rst = hap(10,20)
# print(rst)
# fn()
# fn()
# fn()
