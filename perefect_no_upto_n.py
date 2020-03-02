def prie(no):
    count=0
    for i in range(2,no//2+1):
        if no%i==0:
            count+=1
            break
    if count==0 and no!=1:
        print(no)













def perfect_no_upto_n(no):
    sums=0
    for i in range(1,no):
        if (no%i)==0:

            sums+=i
    if sums==no:
        print('perfect no',no)




for i in  range(1,1000):
    r=perfect_no_upto_n(i)
    r1=prie(i)