my1 = [10, 20, 30, 40, 50.23]
my = [10, 20, 30, 40, 50, 20]

print(my)
print(my[0])
print(my[1:4])
my.append(60)
print(my)
my.insert(6, 70)
print(my)

print()
my.remove(10)
print(my)

my.pop(1)
print(my)

print()
del(my[0])
print(my)


my.insert(6, 70)
print(my.count(70))
print(len(my))

my[0] = 100
print(my)
# for a in my:
#     print(type(a))
