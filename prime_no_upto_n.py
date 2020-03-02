def prime_no_upto_n(no):
    count=0
    for i in range(2,no//2+1):
        if no%i==0:
            count+=1
            break
    if count==0 and no!=1:
        print(no)


for i in range(1,1000):
    r=prime_no_upto_n(i)