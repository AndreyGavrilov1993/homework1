import random
import copy

def bubble_sort(list):
    counter=0
    for j in range(len(list)-1):
        flag=True
        for i in range(len(list)-1-j):
            counter+=1
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
                flag=False
        if flag: break
    return counter

def bubble_sort_bad(list):
    counter=0
    for j in range(len(list)-1):
        for i in range(len(list)-1-j):
            counter+=1
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
    return counter

def shaker_sort(list):
    counter=0
    min=0
    max=len(list)-1
    while(min<max):
        flag=True
        for i in range(max):
            counter+=1
            if(list[i]>list[i+1]):
                list[i],list[i+1]=list[i+1],list[i]
                flag=False
        if (not flag):
            max -= 1
            flag=True
            for i in range(max, min, -1):
                counter+=1
                if (list[i] < list[i - 1]):
                    list[i], list[i - 1] = list[i - 1], list[i]
                    flag=False
            min+=1
        if flag: break

    return counter

def shaker_sort_bad(list):
    counter=0
    min=0
    max=len(list)-1
    while(min<max):
        for i in range(max):
            counter+=1
            if(list[i]>list[i+1]):
                list[i],list[i+1]=list[i+1],list[i]
        max-=1
        for i in range(max, min, -1):
            counter+=1
            if (list[i] < list[i - 1]):
                list[i], list[i - 1] = list[i - 1], list[i]
        min+=1
    return counter

def insertion_sort(list):
    counter=0
    for i in range(1, len(list)):
        for j in range(i, 0, -1):
            counter+=1
            if (list[j]<list[j-1]):
                list[j],list[j-1]=list[j-1],list[j]
            else: break
    return counter
def selection_sort(list):
    counter=0
    for i in range(len(list)-1):
        min = list[i]
        minIndex = i
        for j in range (i, len(list)):
            counter+=1
            if (min>list[j]):
                min=list[j]
                minIndex=j
        list[i], list[minIndex]=list[minIndex], list[i]
    return counter

list = [random.randint(10,99) for i in range(10)]
list2=list.copy()
list3=list.copy()
list4=list.copy()
list5=list.copy()
list6=list.copy()
print(list)
print("bubble sort BAD")
print(bubble_sort_bad(list))
print(list)
print("bubble sort")
print(bubble_sort(list2))
print(list2)
print("shaker sort BAD")
print(shaker_sort_bad(list3))
print(list3)
print("shaker sort")
print(shaker_sort(list4))
print(list4)
print("insertion sort")
print(insertion_sort(list5))
print(list5)
print("selection sort")
print(selection_sort(list6))
print(list6)


#https://proglib.io/p/sort-gif

