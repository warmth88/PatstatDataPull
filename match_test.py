#!/usr/bin/env python
# import csv
import unicodecsv as csv
from fuzzywuzzy import process

name_dest = []
with open('name_list_condense.csv', 'rb') as f_dest:
    f_dest = csv.reader(f_dest, delimiter=',', encoding='utf-8')
    for i in f_dest:
        name_dest.append(i[0])

name_source = []
with open('name_list_std_condense.csv', 'rb') as f_source:
    f_source = csv.reader(f_source, delimiter=',', encoding='utf-8')
    for i in f_source:
        name_source.append(i[0])

print 'ok'
for i in name_dest[:100]:
    sep = 10000
    tmp_max = 0
    for i in range(len(name_source)/sep+1):
        print i
        tmp = process.extractOne(i, name_source[i*sep: (i+1)*sep])
        if tmp_max < tmp[1]:
            tmp_value = tmp
    print tmp_value
