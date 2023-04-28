# Напишите программу, которая на вход принимает два числа A и B, и возводит число 
# А в целую степень B с помощью рекурсии.
A=int(input('A: '))
B=int(input('B: '))
C=A
count1=0
def STPN(A, count1,C):
    if count1==B:
        return A
    return STPN(A*C, count1+1,C)


print(STPN(A,0,C))