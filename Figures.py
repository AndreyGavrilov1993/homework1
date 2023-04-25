print("Есть треугольники под буквами от 'а' до 'к'")
x=input("Выберите треугольник: ").lower()
    #a
if x=="а":
    n=int(input("Длина основания: "))
    a=1
    print("*"*n)
    for i in range(n-1,0,-1):
        print(" "*a + "*"*i)
        a+=1
elif x == "б":
    #б
    n=int(input("Длина основания: "))
    for i in range(1,n+1):
        print("*"*i,end=" ")
        print()
elif x == "в":
    #в
    n=int(input("Длина основания: "))
    a=1
    for i in range(n,0,-2):
        print(" "*a + "*"*i +" "*a )
        a+=1
elif x == "г":
    #г
    n=int(input("Длина основания: "))
    for i in range(n//2 +1 ):
        print(" "*(n - i) + "*"*(1+i*2))
elif x == "д":
    #д
    n=int(input("Длина основания: "))
    a=1
    count=0
    print("*"*n)
    for i in range(n-1,1,-2):
        print(" " * a + "*" * (i-1) + " "*a )
        a+=1
        count=a
    if n%2==0:
        for j in range(2,n+2,2):
            print(" "*(count-1) + "*"*(j))
            count-=1
    else:
        for j in range(1,n+2,2):
            print(" "*(count-1) + "*"*(j))
            count-=1
elif x == "е":
    #e
    n=int(input("Длина основания: "))
    if n%2==0:
        a=n
    else: a=n-1
    for i in range(1,n//2 + 2):
        print("*"*i + " "*a+"*"*i)
        a-=2
    for j in range(n//2,0,-1):
        print("*"*j + " "*(a+4) + "*"*j)
        a+=2
elif x == "ж":
    #ж
    n=int(input("Длина основания: "))
    for i in range(1,n//2 + 2):
        print("*" * i)
    for j in range(n//2,0,-1):
        print("*"*j)
elif x == "з":
    #з
    n=int(input("Длина основания: "))
    a=n//2
    for i in range(1,n//2 + 2):
        print(" "*a  + "*" * i)
        a-=1
    for i in range(n//2,0,-1):
        print(" "*(a+2) + "*" * i)
        a+=1
elif x == "и":
    #и
    n=int(input("Длина основания: "))
    for i in range(n,0,-1):
        print("*"*i)
elif x == "к":
    #к
    n=int(input("Длина основания: "))
    for i in range(1,n+1):
        print(" "*(n-i) + "*"*i)
else:
    print("Треугольника под такой буквой нет")