import random

a=random.randint(1,99)
count=0
while True:
    if count==7:
        break
    count+=1
    n=int(input())
    print(f"осталось попыток {7-count}")
    if n==0:
        break
    elif (n==a):
        print("Круто")
    elif(a<n):
        print("n>загаданного числа")
    elif (a>n):
        print("n<загаданного числа")
print(a)