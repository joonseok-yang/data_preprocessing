a=5
b = None
#모두 True
# rst = a>0 and a==0
#모두 False ==>False
# rst = a>0 or a==0
rst = not a>0
print(rst)
# 0, None, '', [], {}  ==>False

rst = not [10]
print(rst)

my = [10, 20, 30]
print(10 in my)

s = 'hello korea'

print('llo' in s)

d = {'a': 1, 'b': 2, 'c': 3, 0: 1}

print(1 in d.values())

