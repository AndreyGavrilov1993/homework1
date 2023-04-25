#1
# a=('s','g','k','l','o')
# b=('u','r','k','q','o')
# c=('d','i','k','f','o')
# res=tuple(set(a) & set(b) & set(c))
# print(f'элементы, которые есть во всех кортежах',res)

#2
# def get_uniq(numbers:tuple)->list:
#     set1=set()
#     set2=set()
#     for number in numbers:
#         if number not in set1:
#             set1.add(number)
#         else:
#             set2.add(number)
#     return [number for number in numbers if number in set1-set2]
#
# a=(2,5,3,6,7,5,2,1,5,7,8,8,53,2,74,6)
# print(get_uniq(a))

#3
def find_match(*args):
    return tuple(len(set(arg))==1 for arg in zip(*args))

tup1 = (1, 1, 7, 4, 5)
tup2 = (2, 1, 7, 3, 5)
tup3 = (2, 3, 7, 3, 5)
assert find_match(tup1,tup2,tup3)==(0,0,1,0,1)

print(find_match(tup1,tup2,tup3))