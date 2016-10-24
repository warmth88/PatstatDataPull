#!/usr/bin/env python
import csv


def get_info(path):
    with open(path, 'rb') as f:
        f_reader = csv.reader(f, delimiter=',')
        f_reader.next()
        for i in f_reader:
            if i[1] != '':
                f1_writer.writerow([i[0], i[1]])
            else:
                print "no name"
                print i
            if i[-1] != '':
                f2_writer.writerow([i[0], i[-1]])
            else:
                print "no std name"

f1_out = open('name_list.csv', 'wb')
f2_out = open('name_list_std.csv', 'wb')
f1_writer = csv.writer(f1_out, delimiter=',')
f2_writer = csv.writer(f2_out, delimiter=',')
get_info('data/tls206_part01.txt')
print "done"
get_info('data/tls206_part02.txt')
print "done"
