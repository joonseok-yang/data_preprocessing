
def fn():
    print('fn...')

def my( aa ):
    aa()

my( fn )


def my1():
    return fn


rst = my1()
rst()

