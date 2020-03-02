def perefct_no(no):
    sus=0
    for i in range(1,no):
        if no%i==0:
            sus+=i
    if sus==no:
        return True
    else:
        return False
s=int(input('enter the perfect '))
d=perefct_no(s)
if d:
    print('it is perfect no')
else:
    print('not an perfect no')