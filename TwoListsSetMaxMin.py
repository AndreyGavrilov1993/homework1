from random import randrange
a=[randrange(1,11) for i in range(1,11)]
b=[randrange(1,11) for i in range(1,11)]
a.extend(b)
print("содержимое двух списков с повторениями",a)
a1=set(a)
print("содержимое двух списков без повторений",a1)
a=[randrange(1,11) for i in range(1,11)]
b=[randrange(1,11) for i in range(1,11)]
a2=list(set(a) & set(b))
print("общие элементы 2 списков",a2)
a=[randrange(1,11) for i in range(1,11)]
b=[randrange(1,11) for i in range(1,11)]
c=[]
for i in a:
 for j in b:
  if i not in b:
   if j not in a:
    c.append(i)
print("Уникальные элементы списка: ",set(c))
print("Максимальное число списка 1:",max(a),"Минимальное число списка 1:",min(a),"Максимальное число списка 2:",max(b),"Минимальное число списка 2:",min(b))
