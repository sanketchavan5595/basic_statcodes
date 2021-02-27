import math
def npr(n, r):
    return math.factorial(n)/math.factorial(n-r)
def ncr(n, r):
    return math.factorial(n)/(math.factorial(n-r)*math.factorial(r))

print('Menu \n1. npr \n2. ncr \n3. Binomial probability')
ch = int(input('enter your choice: '))
if ch == 1:
    num = int(input('enter n: '))
    r_ = int(input('enter r: '))
    print(npr(num, r_))
elif ch == 2:
    num = int(input('enter n: '))
    r_ = int(input('enter r: '))
    print(ncr(num, r_))
else:
    n = int(input('enter the number of trials: '))
    x = int(input('enter the number for a specific outcome within n trials: '))
    p = float(input('enter the probability of success in a single trial: '))
    q = 1-p
    P = ncr(n,x) * (p**x) * (q**(n-x))
    print('the probability is {}'.format(P))

