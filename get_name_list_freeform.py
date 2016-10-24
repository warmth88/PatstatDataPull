#!/usr/bin/env python
import csv


def get_info(path):
    with open(path, 'rb') as f:
        f_reader = csv.reader(f, delimiter=',')
        f_reader.next()
        for i in f_reader:
            if i[4] != '' or i[5] != '' or i[6] != '' or i[7] !='':
                f_writer.writerow([i[1]] + i[4:8])
            else:
                print "no freeform"
                print i

f_out = open('name_list_freeform.csv', 'wb')
f_writer = csv.writer(f_out, delimiter=',')
get_info('data/tls226_part01.txt')
print "done"
get_info('data/tls226_part02.txt')
print "done"
get_info('data/tls226_part03.txt')
print "done"
