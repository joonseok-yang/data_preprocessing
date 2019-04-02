

while True:
    try:
        score = int(input("score: "))
        if 90 <= score <= 100:
            print("score: " + str(score) + " => A")
        elif 80 <= score <= 89:
            print("score: " + str(score) + " => B")
        elif 70 <= score <= 79:
            print("score: " + str(score) + " => C")
        elif 60 <= score <= 69:
            print("score: " + str(score) + " => D")
        else:
            print("score: " + str(score) + " => F")
    except ValueError:
        break
