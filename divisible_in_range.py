def  divisible_of_range(l,m,divisible):
    d=[]
    for i in range(l,m+1):
        if i%divisble==0:
            d.append(i)
    return d





lower,upper=map(int,input('enter the two values').split(' '))
divisble=int(input('enter the divisble here'))
d=divisible_of_range(lower,upper,divisble)
for i in d:
    print(i)