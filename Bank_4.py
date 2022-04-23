from datetime import datetime

#Простые проценты

def get_delt_days(str_d1,str_d2):

    # convert string to date object
    d1 = datetime.strptime(str_d1, "%Y/%m/%d")
    d2 = datetime.strptime(str_d2, "%Y/%m/%d")

    # difference between dates in timedelta
    delta = d2 - d1
    print(f'Difference is {delta.days} days')
    return delta.days

def simple_percent_days(P,i,n,T = 360):
    S = P*(1+(i*n)/T)
    return S

def complex_percent_days(P,i,n,m,T = 360):
    S = P*((1+(i*n)/(T*m))**m)
    return S

def complex_percent_days_deposit(S,i,n,m,T = 360):
    return(S/pow((1+(i*n)/(T*m)),4))


def Task_4():
    days = get_delt_days('2022/03/20', '2022/06/17')
    deposit = 2000
    percent = 18 / 100

    print(f'England system {simple_percent_days(deposit, percent, days, 365)}')
    print(f'France system {simple_percent_days(deposit, percent, days)}')
    print(f'German system {simple_percent_days(deposit, percent, days - 2)}')

def Task_8():
    deposit = 10000
    percent = {90:14/100,180:16/100,360:17/100}
    ans = []

    for x,y in percent.items():
        ans.append(simple_percent_days(deposit,y,x)-deposit)
        print(f'For {x} days with {int(y*100)}% = {ans[-1]}')

def Task_9():
    deposit = 300000
    percent = {25 / 100 : 180, 20 / 100 : 90, 15 / 100 : 90}
    ans = []

    for x,y in percent.items():
        ans.append(simple_percent_days(deposit,x,y)-deposit)
        print(f'For {y} days with {int(x*100)}% = {ans[-1]}')
    print(f"Summary of accrued per cents {sum(ans)}")

def Task_12():
    days = get_delt_days('2020/01/01', '2020/07/01')
    deposit = 2000
    percent = 12 / 100

    print(f'England system {round(simple_percent_days(deposit, percent, days, 366),2)}')

def Task_14():
    deposit = 10000
    percent = 10 / 100

    print(f"The amount of the deposit during 3 years: {round(complex_percent_days(deposit,percent,m = 3, n = 1080),2)}")

def Task_16():
    deposit = 50000
    percent = 7 / 100
    r = deposit*1.5
    i = 0

    while deposit < r:

        deposit = round(complex_percent_days(deposit,percent,m = 1, n = 360),2)
        print(f'For {i+1} year deposit = {deposit}')
        i += 1

    print(f'Answer is {i}')


def Task_19():
    deposit_1,deposit_2 = 2800,2900
    percent = 13/100

    ans_1 = round(complex_percent_days(deposit_1,percent,m = 3, n = 1080),2)
    print(f"The result of first deposit {ans_1}")
    ans_2 = round(complex_percent_days(deposit_2, percent, m=4, n=1440), 2)
    print(f"The result of second deposit {ans_2}")

    if ans_1 > ans_2:
        print(f"First deposit is more profitable")
    else:
        print(f"Second deposit is more profitable")

def Task_21():
    S = 20000
    percent = 10/100
    ans = round(complex_percent_days_deposit(20000, percent, n = 1440, m = 4),2)
    print(f'The amount of money of the investor is: {ans}')

