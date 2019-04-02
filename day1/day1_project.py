

# 1. 키와 몸무게를 입력받아 비만도를 구하고 결과를 출력하시요(함수를 만드시요)
# 표준체중(kg)=(신장(cm)-100)×0.85
# 비만도(%)=현재체중/표준체중(%)×100
#
# 비만도가90%이하
# 저체중,
# 90초과~110%
# 정상,
# 110초과~120%
# 과체중,
# 120%초과
# 비만


def obesity_check():
    height = float(input("Height: "))
    weight = float(input("Weight: "))

    metric = obesity_metric(height, weight)

    if metric <= 90:
        print("low weight")
    elif 90 < metric <= 110:
        print("normal")
    elif 110 < metric <= 120:
        print("high weight")
    else:
        print("obesity")


def std_weight(h):
    return (h - 100) * 0.85


def obesity_metric(h, w):
    return w / std_weight(h) * 100


# 2. 년도 입력받아
# 1) 윤년여부를 출력하시요
# 윤년의 조건
# 1-1) 4로 나눠 떨어지지만 100으로 나눠 떨어지지 않아야 한다 또는
# 1-2) 400 으로 나눠 떨어지면 윤년임
# 2) 나이를 출력하시요
# 3) 띠(12지신)를 출력하시요

def year_check():
    year = int(input("Input your birth year: "))

    if leap_year_check(year):
        print("your birth year is a leap year")
    else:
        print("your birth year is a not leap year")

    print("Your age is " + str(get_age(year)))

    print("Your zodiac sign is " + get_zodiac_sign(year))


def leap_year_check(y):
    leap_year = False
    if y % 4 == 0 and y % 100 != 0:
        leap_year = True
    elif y % 400 == 0:
        leap_year = True

    return leap_year


def get_age(y):
    return 2019 - y


def get_zodiac_sign(y):
    CALIBRATE = 4
    zodiac_signs = ("rat", "ox", "tiger", "rabbit", "dragon",
                    "snake", "horse", "sheep", "monkey", "rooster",
                    "dog", "pig")

    y = y - CALIBRATE
    return zodiac_signs[y % 12]


# 3. 점수를 입력받아
# 90~100 'A'
# 80~89 'B'
# 70~79 'C'
# 60~69 'D'
# 나머지 'F'
# 딕셔너리를 이용하여 구하시요

def calc_grade():
    # d = {'A': [90, 100], 'B': [80, 89], 'C': [70, 79], 'D': [60, 69]}
    d = {10: 'A', 9: 'A', 8: 'B', 7: 'C', 6: 'D'}

    score = int(input("Enter score: "))
    return d.get(score//10, 'F')


# 4. m 를 입력받아 마일로 변환하시요(함수를 만드시요)
def meter_to_mile():
    meter = float(input("Enter meter: "))
    return 0.000621371 * meter


# 5. 화씨 를 입력받아 도로 변환하시요(함수를 만드시요)
def fahrenheit_to_celsius():
    f = float(input("Enter fahrenheit: "))
    return (f - 32) * (5/9)


# 6. 하나의 정수를 입력받아 약수를 구하는 함수를 만드시요.
def get_aliquots():
    subject = int(input("Enter integer: "))
    values = set()
    for n in range(1, subject // 2 + 1):
        # print(n)
        if subject % n == 0:
            # print("insert: " + str(n) + ", " + str(subject // n))
            values.add(n)
            values.add(subject // n)

    return sorted(values)


# 7. 2개의 정수를 입력받아 절대값의 합을 구하는 함수를 만드시요
def abs_sum():
    i1 = int(input("Enter integer1: "))
    i2 = int(input("Enter integer2: "))

    fcn = lambda v: v if v >= 0 else v * -1

    return fcn(i1) + fcn(i2)


# 8. map 함수와 동일한 기능을 하는 mymap 함수를 구현하시요.
def mymap(key, iterable):
    return [key(x) for x in iterable]


# 1
print("\nLet's check obesity!!")
obesity_check()

# 2
print("\nYour birth year information")
year_check()

# 3
print("\ngrade calculating")
print(calc_grade())

# 4
print("\nmile converting")
print(meter_to_mile())

# 5
print("\ncelsius converting")
print(fahrenheit_to_celsius())

# 6
print("\ngetting aliquots")
print(get_aliquots())

# 7
print("\nabs sum test")
print(abs_sum())

# 8
print("\nTest mymap")
print(mymap(lambda v: v+2, [10, 20, 30]))
