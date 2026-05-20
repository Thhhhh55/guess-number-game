answer = 100
while True:
    guess = int(input("猜一个数字:"))
    if guess > answer:
        print("猜大了")
    elif guess < answer:
        print("猜小了")
    else:
        print("猜对了")
        break