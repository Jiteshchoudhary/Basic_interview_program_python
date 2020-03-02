def sums_of_digits(no):
    sums=0
    while no!=0:
        reminder=no%10
        sums+=reminder
        no=no//10
    return sums
a=12345
print(sums_of_digits(a))