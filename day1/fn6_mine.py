data = [10, 20, 30, 40, 50]
print(id(data))
print(id(filter(lambda v: v > 29, data)))
f = filter(lambda v: v > 29, data)

print(list(f))

m = map(lambda v: v + 2, data)
print(list(m))


my = "10", "20", "30"
print(list(my))

m = map(lambda v: int(v), my)

m = map(int, my)

print(list(m))
