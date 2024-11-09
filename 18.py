n1 = int(input("number1: "))
n2 = int(input("number2: "))
n3 = int(input("number3: "))

def sum_nad_dif():
    sum1 = n1 + n2 + n3
    if sum1 % 2 == 0:
        print(sum1, sum1, sum1)
    else:
        print(sum1, "are odd")

sum_nad_dif()
