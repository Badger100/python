number = 17

given_number = int(input("Enter number: "))


def twice():
    difference = given_number - number

    if given_number > number:
        doub_dif = difference * 2
        print(doub_dif)
        return
    print("your entity les than", number, "difference is", difference)
twice()
