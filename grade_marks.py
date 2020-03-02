def grade_marks(a,b,c,d,e,avg):
    if (avg >50) and (avg<60):
        return 'B'
    elif (avg >60 )and (avg<70):
        return 'A'
    elif (avg>70) and (avg<80):
        return 'A+'
    else:
        return 'Nothing'







a,b,c,d,e=list(map(int,input().split(' ')))
s=(a+b+c+d+e)
l=5
avg=s/l
print(grade_marks(a,b,c,d,e,avg))
