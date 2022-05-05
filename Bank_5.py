def Ant_Year(S,i,n):
    i =i
    k = i*((1+i)**n)/(((1+i)**n)-1)
    a = k*S
    return a
def Ant_month(S,i,n):
    i =i/12
    k = i*((1+i)**n)/(((1+i)**n)-1)
    a = k*S
    return a
def Dif(S,i,N):
    ans = 0
    for n in range(N):
        b = S/N
        Sn = S-(b*n)
        p = Sn*i/12
        ans += b+p
        if n == 11:
            return ans
def Dif_2(S,i,N):
    ans = []
    for n in range(N):
        b = S/N
        Sn = S-(b*n)
        p = Sn*i/12
        ans.append(b+p)

    return ans

#Dif(100000,0.1,6)
#print(Ant_month(30000,0.18,36))

def Task_1(S,n,i):
    ans = []
    for x in range(n):
        k = (i * ((1 + i) ** n) / (((1 + i) ** n) - 1))
        S = S * 1.125
        A = k*S
        ans.append(A)
    print(f'Bank profit on this loan is {sum(ans)-S}')
def Task_2(S,A,n,i):
    k = (i * ((1 + i) ** n) / (((1 + i) ** n) - 1))
    while k*S > A:
        S = S*1.01
        n += 1
        k = (i * ((1 + i) ** n) / (((1 + i) ** n) - 1) )
    print(Ant_month(S, 0.01, n))
    print(f'The amount of the minimum number of months is {n} months')
def Task_4():
    print(f'The sum of the first 12 months{round(Dif(2400000,0.03,24),2)}')
def Task_12():
    ans = Dif_2(750000,0.18,8)
    for x in range(len(ans)):
        print(f'Result for the month № {x+1} is {ans[x]}')
    print(f'Overall payment is {sum(ans)}')
    print(f'Profit of the bank is {sum(ans)-750000}')

#Task_1(680000,2,0.125)
#Task_2(1100000,275000,1,0.01)
#Task_4()
#Task_12()
