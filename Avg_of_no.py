# python program to find the avg of the no
# formula is avg=totalsum/no of observations
a=[1,3,43,434,23,345,324,45]
sums=0
lengths=0
for i in a:
    sums+=i
    lengths+=1

print(sums)
print('avg is \t',sums/lengths)