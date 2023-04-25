#1
s=input("Введите выражение: ")
if s.find("+") !=-1:
    n=s.find("+")
    print(s,"=",float(s[:n])+float(s[n+1:len(s)]))
if s.find("-")  !=-1:
    n=s.find("-")
    print(s,"=",float(s[:n])-float(s[n+1:len(s)]))
if s.find("*")  !=-1:
    n=s.find("*")
    print(s,"=",float(s[:n])*float(s[n+1:len(s)]))
if s.find("/")  !=-1:
    n=s.find("/")
    print(s,"=",float(s[:n])/float(s[n+1:len(s)]))
#2
'''import random
res=[random.randrange(-5000, 5000) for i in range(10)]
print ("рандомный списочек чисел: " + str(res))
a=max(res)
print("максимальное число: ",a)
b=min(res)
print("минимальное число: ",b)
i=0
print('cумма положительных чисел:', sum(i>0 for i in res))
print('сумма отрицательных чисел:', sum(i<0 for i in res))
print('кол-во нулей чисел:', sum(i==0 for i in res))'''