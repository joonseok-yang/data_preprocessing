# a = int(input("Input: "))
#
# while a <= 5:
#     print(a)
#     a += 1

# a = input("Input: ")
#
# for n in a:
#     print(n)
#
# my = [10, 20, 30, 40]
#
# for n in my:
#     print(n)

d = {'a': 1, 'b': 2, 'c': 3, 'd': 1}

print('key')
for n in d:
    print(n)

print()
print('value')
for n in d.values():
    print(n)

print()
print('item tuples')
for n in d.items():
    print(n)

print()
print('item unpacking')
for k, v in d.items():
    print(k, v)
