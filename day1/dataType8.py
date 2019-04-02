d = {'a': 1, 'b': 2, 'c': 3, 0: 1}

print(d)
print(d['a'])
d['b'] = 20
print(d['b'])
print(d.keys())
print(d.values())
print(d.items())
print(d.get('aa', 0))  # can provide default value for invalid key
# print(d.fromkeys(d, 0))
print()
d.pop('b')
print(d)

# d.pop('a')
del(d['a'])
print(d)


# print(type(d))
