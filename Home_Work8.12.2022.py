'''#1
day=int(input("введите номер дня недели 1-7: "))
if day==1:
    print("понедельник")
elif day==2:
    print("вторник")
elif day==3:
    print("среда")
elif day==4:
    print("четверг")
elif day==5:
    print("пятница")
elif day==6:
    print("суббота")
elif day==7:
    print("воскресенье")
else:
    print("неверно")'''
'''
#2
month=int(input("введите номер месяца 1-12: "))
if month==1:
    print('Январь')
elif month==2:
    print('Февраль')
elif month==3:
    print('Март')
elif month==4:
    print('Апрель')
elif month==5:
    print('Май')
elif month==6:
    print('Июнь')
elif month==7:
    print('Июль')
elif month==8:
    print('Август')
elif month==9:
    print('Сентябрь')
elif month==10:
    print('Октябрь')
elif month==11:
    print('Ноябрь')
elif month==12:
    print('Декабрь')
else:
    print("неверно")'''
'''
#3
n=int(input("введите число: "))
if n>0:
    print("Number is positive")
elif n<0:
    print("Number is negative")
elif n==0:
    print("Number is equal to zero")
else:
    print("неверно")'''
#4
a=int(input("введите 1-е число: "))
b=int(input("введите 2-е число: "))
if a==b:
    print("Числа равны")
else: print(min([a,b]),max([a,b]))   

