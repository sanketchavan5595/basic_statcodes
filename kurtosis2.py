import pandas as pd
import numpy as np
def dot():
    print("**********************************************************")
def line():
    print("-----------------------------------------------------------------------")

x_list = []
freq_list = []
t = int(input("enter the total number of entries: "))
h = float(input("enter the class width: "))
f1 = float(input("enter the first lower limit: "))
x_list = [f1]
for i in range(t - 1):
    f1 += h
    x_list.append(f1)
dot()
for i in range(t):
    freq = float(input("enter frequencies: "))
    freq_list.append(freq)

my_dict = {"x": x_list, "freq": freq_list}
file = pd.DataFrame(my_dict)

# for adding serial numbers to the dataset
def setIndex(df):
    df['sr_no'] = np.arange(1, df.shape[0] + 1)
    df.set_index('sr_no', inplace=True)
setIndex(file)

l1 = list(file.x)
a = l1[int((len(l1)-1)/2)]
file['u'] = (file.x - a) / h
file['fu'] = file.freq * file.u
file['fu2'] = file.freq * (file.u**2)
file['fu3'] = file.freq * (file.u**3)
file['fu4'] = file.freq * (file.u**4)

line()
print('sum of frequency: {}'.format(file.freq.sum()))
print('sum of fu: {}'.format(file.fu.sum()))
print('sum of fu2: {}'.format(file.fu2.sum()))
print('sum of fu3: {}'.format(file.fu3.sum()))
print('sum of fu4: {}'.format(file.fu4.sum()))

line()
u_1 = h * (file.fu.sum()/file.freq.sum())
u_2 = (h**2) * (file.fu2.sum()/file.freq.sum())
u_3 = (h**3) * (file.fu3.sum()/file.freq.sum())
u_4 = (h**4) * (file.fu4.sum()/file.freq.sum())
print('u_1: {}'.format(u_1))
print('u_2: {}'.format(u_2))
print('u_3: {}'.format(u_3))
print('u_4: {}'.format(u_4))
line()

# central moments
u1 = 0
u2 = u_2 - (u_1**2)
u3 = u_3 - (3*u_2*u_1) + (2*(u_1**3))
u4 = u_4 - (4*u_3*u_1) + (6*u_2*(u_1**2)) - (3*(u_1**4))
print('central moments are: ')
print('u1: {}'.format(u1))
print('u2: {}'.format(u2))
print('u3: {}'.format(u3))
print('u4: {}'.format(u4))
line()

B1 = (u3**2)/(u2**3)
B2 = (u4)/(u2**2)
print('coefficent of skewness is: {}'.format(B1))
print('coefficent of kurtosis is: {}'.format(B2))

if B2<3:
    print("the distribution is platykurtic")
elif B2>3:
    print("the distribution is leptokurtic")
else:
    print("the distribution is mesokurtic")