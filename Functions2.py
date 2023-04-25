#1
# def show_list(list):
#     count=1
#     for i in list:
#         count=count*i
#     return count
#
# print(show_list([1,2,3,4,5]))
import random


#2
# def show_min(n):
#
#     return min(n)
# print(show_min([5,8,7]))

#3
# def show_simple(s):
#     simple=0
#     for i in s:
#             k=2
#             while k*k<=i:
#                 if  i%k==0:
#                     return  i, "составное число"
#                     break
#                 k+=1
#             else:
#                 simple+=1
#                 return i,"простое число"
#     if simple !=0:
#             return "Количество простых чисел: ", simple
#     else:
#             return "Простых чисел нет"
#
# print(show_simple([1,2,3,4,5,6,7,8,9]))

#4
# def show_num(list2,list1):
#     list3=list()
#     for num in list1:
#      if num not in list2:
#       list3.append(num)
#     list1=list3
#     return list1
#
# print(show_num(([5,1]),([1,2,3,4,5,6,7,8,9,10,11,12])))

#5
# def show_total(a1,b1):
#     total=list()
#     total.append(a1)
#     total.append(b1)
#     return total
#
# print(show_total(([5,1]),([1,2,3,4,5,6,7,8,9,10,11,12])))

#6
def show_str(str,result):
    return [i**str for i in result]

print(show_str(5,([1,2,3,4,5])))