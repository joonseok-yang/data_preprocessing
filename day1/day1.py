# problem 1
print ("## problem 1 ##")
height = int(input("키:"))
weight = int(input("몸무계:"))

rate = weight / ((height - 100) * 0.85) * 100

if rate <= 90:
    print("저체중")
elif rate <= 110:
    print("정상")
elif rate <= 120:
    print("과체중")
else:
    print("비만")

# problem 2
print ("## problem 2 ##")
year = int(input("연도:"))
if not year % 400:
    print("윤년")
elif not year % 4 and year % 100:
    print("윤년")
else:
    print("평년")
print("나이:", 2019-year)
animal = ["돼지","개","닭","원숭이","양","말","뱀","용","토끼","범","소","쥐"]

print("띠:", animal[(2019-year)%12])

# problem 3
print ("## problem 3 ##")
score = int(input("점수:"))
d = {'A': (90, 100), 'B': (80, 89), 'C': (70, 79), 'D': (60, 69), 'F': (0, 59)}
for k, v in d.items():
    if v[0] <= score <= v[1]:
        print(k)
        break


# problem 4
print("## problem 4 ##")
def meter2mile(m):
    return m * 0.000621371


m = int(input("미터:"))
print("마일:", meter2mile(m))


# problem 5
print("## problem 5 ##")
def ftoc(f):
    return (f - 32) / 1.8


f = int(input("화씨:"))
print("섭씨:", ftoc(f))


# problem 6
print("## problem 6 ##")
number = int(input("정수:"))

yak = set()
for n in range(1,number+1):
    if number%n == 0:
        yak.add(n)
print(sorted(list(yak)))

# problem 7
print("## problem 7 ##")
n1 = int(input("정수1:"))
n2 = int(input("정수2:"))

def myabs(n):
    return n if n > 0 else -1 * n

print(myabs(n1) + myabs(n2))

# problem 8
print("## problem 8 ##")


def mymap(func, dd):
    for d in dd:
        yield func(d)


data = [10, 20, 30]

m = mymap(lambda x: x+2, data)
print(m, list(m))




