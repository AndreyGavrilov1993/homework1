#1
'''
a=int(input("Первое число: "))

b=int(input("Второе число: "))

for i in range(a,b+1):

  if i%7==0:

      print(i)'''
#2
'''
a=int(input("Первое число: "))

b=int(input("Второе число: "))

c=[i for i in range(a,b+1)]

print("Все числа диапозона:", str(c).replace("[","").replace("]",""))

c.sort(reverse=True)

print("Все числа диапозона в убывающем порядке:", str(c).replace("[","").replace("]",""))

a=[]

b=0

for i in c:

   if i%7==0:

       a+=[i]

   if i%5==0:

       b+=1

print("Все числа кратные 7:", str(a).replace("[","").replace("]",""))

print("Количество чисел, кратных 5:", str(b).replace("[","").replace("]",""))'''
#3
a=int(input("Первое число: "))

b=int(input("Второе число: "))

for i in range(a,b+1):

   if i%3!=0 and i%5!=0:

       print(i)

   if i%3==0 and i%5==0:

       print("Fizz Buzz")

   else:

       if i%3==0:

           print("Fizz")

       if i%5==0:

           print("Buzz")