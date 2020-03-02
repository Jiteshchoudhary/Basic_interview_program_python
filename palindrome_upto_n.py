def palindrome(no):

    rev=0
    s=no
    while no!=0:
        reminder=no%10
        rev=rev*10+reminder
        no=no//10
    if s==rev:
        print(s)


for i in range(1,100):
    r=palindrome(i)


