'''a=int(input("Введите три цифры: "))
b=str(a)
print("Сформированное число:",b)
a=int(input("Введите четырёхзначное число:"))
a1=(a//1000)
a2=(a%100)//10
a3=(a%10)
a4=(a//100)%10
b=a1*a2*a3*a4
print("Результат произведения чисел:",b)      
meter=float(input("м: "))
santimeter=(meter*100)
decimeter=(meter*10)
milimeter=(meter*1000)
mili=(meter*0.621)
print('сантиметры6 ',santimeter)
print('ециметры',decimeter)
print('миллиметры',milimeter)
print('мили',mili)     
a=float(input("Введите основание треугольника:"))
h=float(input("Введите высоту треугольника:"))
S=0.5*a*h
print("Площадь треугольника = :", S) '''
x=int(input("Введите четырёхзначное число:"))
x1=x%10
x2=(x//10)%10
x3=(x//100)%10
x4=(x//1000)%100
print(x1,x2,x3,x4)     
