def fn():
    print("hello")
    print("korea")


def hap(a, b):
    return a + b


def fn1():
    return 10, 20


f = fn
f()

rst = hap(10, 20)
print(rst)

rst = fn1()

print(rst)
