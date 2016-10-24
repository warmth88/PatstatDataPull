#!/usr/bin/env python
import csv

f1 = open('name_list.csv', 'rb')
f1_reader = csv.reader(f1, delimiter=',')
f2 = open('name_list_freeform.csv', 'rb')
f2_reader = csv.reader(f2, delimiter=',')

name_dic = {}
for i in f1_reader:
    name_dic[i[0]] = i[1]
print "read_1 done"

freeform_dic = {}
for i in f2_reader:
    freeform_dic[i[0]] = i[1]
print "read_2 done"

match = 0
for i in name_dic.keys():
    try:
        if set(name_dic[i].split()) == set(freeform_dic[i].split()):
            match += 1
        else:
            print name_dic[i], freeform_dic[i]
    except:
        pass
    if match % 1000000 == 0:
        print match

print match, "final"
f1.close()
f2.close()
