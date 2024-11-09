n1 = 100
n2 = 1000
n3 = 2000

n4 = int(input("Enter number: "))

def inbetween(number):
    if number >= n1 and number < n2:
        print("Number in between ", n1, "and", n2)
    elif number >= n2 and number <= n3:
        print("Number in between ", n2, "and", n3)
    else:
        print("Out of range")
    return
inbetween(n4)
