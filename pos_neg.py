def positive_or_neg(n):
    if n>0:
        return 'Positive'
    else:
        return 'negative'

a=int(input('enter the no here'))
print(positive_or_neg(a))