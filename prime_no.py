def prime_no(no):
    count=0
    for i in range(2,no//2+1):
        if no%i==0:
            count+=1
            break
    if count==0 and no!=1:
        return True
    else:
        return False


n=int(input('enter a no to check wheather it is prime or not'))
d=prime_no(n)
if d:
    print('no is prime')
else:
    print('not an prime no')