# python program of reverse a no
def Reversed_a_no(n):
    rev=0
    while n!=0:
        reminder=n%10
        rev=rev*10+reminder
        n=n//10
    return rev



i=12345
d=Reversed_a_no(i)
print(d)