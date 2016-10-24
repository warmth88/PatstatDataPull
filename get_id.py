#!/usr/bin/env python
import csv

name_dest = {}
with open('name_list.csv', 'rb') as f_dest:
    f_dest = csv.reader(f_dest, delimiter=';')
    f_dest.next()
    for i in f_dest:
        if (i[1]+' '+i[2]) in name_dest:
            name_dest[i[1]+' '+i[2]].append(i[0])
        else:
            name_dest[i[1]+' '+i[2]] = [i[0]]
print len(name_dest.keys())

# name_source = {}
# with open('name_list_std.csv', 'rb') as f_source:
#     # f_source = csv.reader(f_source, delimiter=',', encoding='utf-8')
#     f_source = csv.reader(f_source, delimiter=',')
#     for i in f_source:
#         if i[1] in name_source:
#             name_source[i[1]].append(i[0])
#         else:
#             name_source[i[1]] = [i[0]]
# 
# print len(name_source.keys())

f_out = open('name_list_condense.csv', 'wb')
f_out = csv.writer(f_out, delimiter=',')
for i in name_dest.keys():
    f_out.writerow([i] + name_dest[i])

# for index, i in enumerate(name_dest.keys()):
#     if index % 10 == 0:
#         print index
#     for j in name_source.keys():
#         if len(i) == len(j):
#             if i == j:
#                 print i, name_dest[i], name_source[j]
