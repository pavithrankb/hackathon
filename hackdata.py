import pandas as pd
import numpy as np
df=pd.read_csv('new.csv')
# print(df)
print('Enter the userid(0-20000)')

uid=int(input())
def fixedcharge(usage):
    if usage>200 & usage<250:
        fx=80
    elif usage>150 & usage<200:
        fx=70
    elif usage>100 & usage<150:
        fx=55
    elif usage>50 & usage<100:
        fx=45
    elif usage <= 50:
        fx=35
    return(fx)


def new250(usage):
    cost=0
    c = [3.7,3.7,4.8,6.4,7.6]
    s = usage
    for i in c:
        if s-50 > 0:
            s-= 50
            cost += (50 * i)
        else:
            cost += (s * i)
            s = 0
    print('The due for this month is rupees:',int(cost+fx))

# print('''enter the type(1 for domestic 2 for industrial...)
#  1.domestic
#  2.industrial
#  3.agriculture
#  4.commercial''')
# type=int(input())
# print('enter the initial and final reading of the meter reading')
# ini,final=map(int,input().split())
# usage=final-ini


for i in df['userid']:
    if i==uid :
        id = i
print('userid:    ',int(df.loc[id,'userid']))
print('type:      ',int(df.loc[id,'type']))

print('''type 1:domestic 
type 2:industrial
type 3:agricultural
type 4:commercial''')
type=int(df.loc[id,'type'])
usage=int(df.loc[id,'powerusage'])

print('your powerusage is ',usage,'kWh')

fx=fixedcharge(usage)
if type==1:
    cost=0
    if usage<=250:
        new250(usage)
    elif usage>500:
        cost=usage*7.9 + 150
    elif usage>400 & usage<500:
        cost = usage * 7.1 + 130
    elif usage>350 & usage<400:
        cost = usage * 6.9 + 120
    elif usage>300 & usage<350:
        cost = usage * 6.6 + 110
    elif usage>250 & usage<300:
        cost = usage * 5.8 + 110
    print('The due for this month is rupees:',int(cost))

elif type==2:
    if usage<10:
        cost=100
    else :
        cost=usage*60
    print('The due for this month is rupees:',int(cost))
elif type==3:
    cost=usage*2.50 +8
    print('The due for this month is rupees:',int(cost))
elif type==4:
    print('1.Single phase(type 1) or 3.three phase(type 3)')
    x=int(input())
    if x==1:
        fx=60
    elif x==3:
        fx=80
    c=[6,6.7,7.4,7.4,8.0]
    s=usage
    if usage<500:
        for i in c:
            if s-100 > 0:
                s-=100
                cost=(100*i)
            else:
                cost+=(s*i)
                s=0
    else:
        cost=usage*9.3
    print('The due for this month is rupees:',int(cost+fx))

input("Press Enter to exit...")
















