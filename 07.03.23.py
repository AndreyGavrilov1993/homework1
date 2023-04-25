# with open("test1.txt", 'r', encoding="utf-8") as file:
#     dict1={}
#     for i in file:
#         list1=i.split(" ")
#         dict1[list1[0]]=list1[1][:-1:]
#
# with open("test2.txt", 'w', encoding='utf-8') as file:
#     for i in dict1.keys():
#         file.write(i+" ")
#     file.write("\n")
#     for i in dict1.values():
#         file.write(i+" ")





# def read_file(path):
#     with open(path, 'r', encoding='UTF-8') as file:
#         file.readline()
#         list = file.readlines()
#         return list
#
#
# def set_clas(list):
#     clas = set()
#     for i in list:
#         clas.add(i[i.rindex(";") + 1:-1:])
#     return clas
#
#
# def create_file(file_name, list):
#     with open(file_name + ".csv", 'w', encoding='UTF-8') as file:
#         for i in list:
#             if (i[i.rindex(";") + 1:-1:] == file_name):
#                 file.write(i[:i.rindex(";"):] + "\n")
#
#
# list1 = read_file("students.csv")
# set1 = set_clas(list1)
# for i in set1:
#     create_file(i, list1)



import csv

data = [{'name': 'Иван', 'clas': '3А', 'phone': '576234'},
       {'name': 'Пётр', 'clas': '5Б', 'phone': '239498'},
       {'name': 'Олег', 'clas': '4А'},
       {'name': 'Ольга', 'clas': '4А'}
       ]
with open('st4.csv', 'w', newline='', encoding='UTF-8') as file:
    writer = csv.DictWriter(file, fieldnames=list(data[0].keys()), delimiter=';', qouting=csv.QUOTE_MINIMAL)
writer.writeheader()
for d in data:
    writer.writerow(d)
# filenames = ["st1.csv", "st2.csv"]
# path = "st3.csv"
# title = "name,clas,phone"
# sep = ","
#
# files = [open(f) for f in filenames]
#
# with open(path, "w") as csvfile:
#     writer = csv.writer(csvfile, delimetr=sep)
#     writer.writerow(title.split(sep))
#     for row in zip(*files):
#         writer.writerow(map(str.strip, row))
#
# files = [f.close() for f in files]


# import pandas as pd
# import glob
#
# files = glob.glob("st3.csv")
# file = ["st1.csv","st2.csv"]
# combined = pd.DataFrame()
# for file in files:
#     data=pd.read_csv(file)
#     data['filename'] = file
#     combined = pd.concat([combined, data])
#     combined[:5]
#     combined.to_csv("combined.csv", index=False, sep=",")



# def read_file(path):
#     with open(path, 'r', encoding='UTF-8') as file:
#         file.readline()
#         list=file.readlines()
#         return list
#
# def set_clas(list):
#     clas=set()
#     for i in list:
#         clas.add(i[i.rindex(";")+1:-1:])
#         return clas
#
# def create_file(file_name, list):
#     with open(file_name + ".csv", 'w', encoding='UTF-8') as file:
#         for i in list:
#             if (i[i.rindex(";")+1:-1:]==file_name):
#                 file.write(i[i.rindex(";"):]+"\n")
#
# list1=read_file("st1.csv")
# set1=set_clas(list1)
# for i in set1:
#    create_file(i, list1)