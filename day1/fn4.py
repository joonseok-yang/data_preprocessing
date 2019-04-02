data = [10, 20, 30, 40, 50]


def fn(v):
    return v > 30


def fn1(v):
    return v <= 30


def myfilter(dt, key):
    # return [n for n in dt if n > 30]
    return [n for n in dt if key(n)]


# rst = myfilter(data, fn)
rst = myfilter(data, fn1)

print(rst)

