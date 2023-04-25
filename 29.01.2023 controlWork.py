#часть 1 (26 баллов)
#1+

# num=int(input("введите первое число: "))
# num2=int(input("введите второе число: "))
# num3=int(input("введите третье число: "))
# num4=int(input("введите четвертое число: "))
# max_num=0
# if num>num2 and num>num3 and num>num4: print(num)
# elif num2>num and num2>num3 and num2>num4: print(num2)
# elif num3>num and num3>num2 and num3>num4: print(num3)
# elif num4>num and num4>num2 and num4>num3: print(num4)

#2+

# n=int(input())
# n1=int(input())
# for i in range(n,n1+1):
#     if i%i==0:
#         print(i, end=" ")

#3+

# size=5
# for i in range(size):
#     print("*\t"*size)


#4+

# pr=1
# for i in range(40,85+1):
#     pr*=i
# print(pr,end=" ")

#5+

#
# list=list(range(1,10))
# for i in list:
#     print(i,end=" ")

#6+
# sum=0
# list=list(range(1,10+1))
# print(list)
# print(len(list))
# for i in list:
#     sum+=i
# print(sum/len(list))

#часть 2 (34 баллa)

#1+
# text="Сегодня 21.11.2020 год. Завтра будет новая встреча"
# count=0
# list=list(text)
# for i in list:
#     if i==" " : count+=1
#     elif i==text.isdigit(): count-=1
# print(f"{count} слов")

#2.2+
#list8=[]
#summ=0
#while True:
#    num=input("Введите число или введите \"Cтоп\" для окончания ввода: ")
 #   if num.upper()=="СТОП":
#        print(list8)
 #       print(summ)
 #       break
  #  try:
 #       list8.append(int(num))
  #     summ+=int(num)
 #   except:
#        print("Некорректное значение")

#2.3+

#list1=["кот","рыба","фонарь","пёс","морс","дерево","ложка","стол","тыква","стул"]
#list2=["пёс","фонарь","тыква"]
#print(list1)
#print(list2)
#list3=list()
#for num in list1:
#  if num not in list2:
#   list3.append(num)
#list1=list3
#print(list1)

#Part3

#3.1+

#list31=[]
#while True:
 #   v=input("1-add | 2-del | 3-show | 4-summ")
#    if v=="1":
 #       listBuf=[]
 #       listBuf.append(input("input name: "))
 #       listBuf.append("input price: ")
 #       list31.append(listBuf)
 #   elif v=="2":
 #       num31=int(input())
  #      list31.pop(num31)
 #   elif v=="3":
 #       for i in list31:
 #           print(f"{i[0]}: {i[1]}")
#    elif v=="4":
 #       summ=0
 #       for i in list31:
  #          summ+=i[1]
 #       print("summ:", sum)
 #   else: print("error. Try again")