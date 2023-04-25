list1=[1,2,3,4,5,6,7,8,9,7,5,3,8,4,1]

def sum_min(list, n, minimum=0, min_index=0, index=0, flag=True):
    summ=0
    if(flag):
        for i in range(n):
            summ+=list[i]
        index=0
        minimum=summ
    else:
        try:
            for i in range(index, n+index,):
                summ+=list[i]
        except:
            return min_index
        if(minimum>summ):
            minimum=summ
            min_index=index
    return (sum_min(list, n, minimum, min_index, index+1, False))
print(sum_min(list1,3))