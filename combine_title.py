#!/usr/bin/env python
# find appln title of certain appln_id list
import csv

title = {}
with open('tmp_title.dat', 'r') as f1:
    for i in f1:
        tmp = i.split()
        title[tmp[0]] = i[len(tmp[0])+1:-1]

f_out = csv.writer(open('added_title.csv', 'w'), delimiter=',',
                   dialect='excel')

with open('/Users/huanxin/Downloads/add_title.csv', 'rb') as f_in:
    header = f_in.readline().split(',')
    print header
    header = header[:12] + ['appln_title'] + header[12:]
    f_out.writerow(header)
    f_in = csv.reader(f_in, delimiter=',')
    for i in f_in:
        try:
            new = i[:12] + [title[i[11]]] + i[12:]
        except:
            print 'err: ', i[11]
            new = i[:12] + [''] + i[12:]
        f_out.writerow(new)
