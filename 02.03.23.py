# import random
#
# def cut(list1, list2):
#     for i in list2:
#         while i in list1:
#             list1.remove(i)
#
# list1 = [ random.randint(1,9) for i in range(10)]
# list2 = [ random.randint(1,9) for i in range(4)]
# print(list1)
# print(list2)
# cut(list1, list2)
# print(list1)

# str = "qwertyui"
#
# list=[]
# for i in range (0,len(str)-1,2):
#     list.append(list[i]+str[i+1])
# if (len(str)%2): list.append(str[len(str)])
# print(list)

import random
set_name={'Вася', 'Петя', 'Оля', 'Маша', 'Таня', 'Юра'}
dict_students={}

def create_marks(dis, marks):
    list1=[]
    for i in range (dis):
        list1.append([random.randint(2,5) for i in range(marks)])
    return list1

for i in range(4):
    buf={tuple(set_name)[i]:create_marks(4,3)}
    dict_students.update(buf)

for key, val in dict_students.items():
    print(f'{key} : {val}')