#!/usr/bin/env python
import csv

name_dest = []
with open('name_list_condense.csv', 'rb') as f_dest:
    f_dest = csv.reader(f_dest, delimiter=',')
    for i in f_dest:
        name_dest.append(i[0])

name_source = []
with open('name_list_std_condense.csv', 'rb') as f_source:
    f_source = csv.reader(f_source, delimiter=',')
    for i in f_source:
        name_source.append(i[0])

overlap = set(name_dest) & set(name_source)
f_out = open('name_match_std.dat', 'w')
for i in overlap:
    f_out.write(i+'\n')
print len(overlap)
f_out.close()
