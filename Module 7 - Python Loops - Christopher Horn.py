def loop():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    for number in numbers:
        if number % 2 == 0:
            print("number " + str(number) + " is even.")
        else:
            print("number " + str(number) + " is odd.")
loop()

