# check wheather no is palindorme or not
def palindrome(no):
    rev=0
    s=no
    while no!=0:
        reminder=no%10
        rev=rev*10+reminder
        no=no//10
    if s==rev:
        return True
    else:
        return False
no=int(input('enter the no here'))
d=palindrome(no)
if d:
    print('no is palindrome')
else:
    print('not an palindrome')