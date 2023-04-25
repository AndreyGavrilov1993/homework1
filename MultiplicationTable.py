'''#1
a=int(input())
for i in range(2,a+1):
    flag=True
    for f in range(2,i):
        if i%f==0:
            flag=False
            break
    if flag:
        print(i,end=" ")'''
'''       
#2
n1=int(input())
n2=input()
a=1
while (a<11):
    b=1
    while (b<11):
        print(b,"*",a,"=",b*a, end="\t")
        b+=1
    a+=1
    print()'''
#3
# n1=int(input())
# n2=input()
a=1
while(a<11):
    b=1
    while(b<11):
        print(b,"*",a,"=",a*b,end="\t\t")
        b+=1
    a+=1
    print()