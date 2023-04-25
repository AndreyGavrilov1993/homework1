'''
#1
a=int(input("введите 1-е число: "))
b=int(input("введите 2-е число: "))
c=int(input("введите 3-е число: "))
op=input("введите операцию :")
if op=="+":
    print(a+b+c)
elif op=="*":
    print(a*b*c)
else:
    print("такой команды нет")'''
#2
a=int(input("введите 1-е число: "))
b=int(input("введите 2-е число: "))
c=int(input("введите 3-е число: "))
op=input("введите операцию sr")
print("наибольшее число :",max(a,b,c))
print("наименьше число :",min(a,b,c))
if op=="sr":
    print("среднеарифметическое :",((a+b+c)/2))
else:
    print("такой команды нет")
    '''
#3    
meter=int(input("введите количество метров :"))
reg=input("введите miles/inch/yard")
if reg=="miles":
    print(1609*meter)
elif reg=="inch":
    print(meter/39.37)
elif reg=="yard":
    print(meter/1.094)'''
