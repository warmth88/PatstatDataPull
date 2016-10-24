#!/usr/bin/env python
# find appln title of certain appln_id list
import csv
import zipfile

appln_id = []
with open('/Users/huanxin/Downloads/add_title.csv', 'rb') as f_in:
    header = f_in.readline()
    print header
    f_in = csv.reader(f_in, delimiter=',')
    for i in f_in:
        appln_id.append(i[11])
print appln_id
print len(appln_id)

appln_title = {}
path = '/Users/huanxin/bianchi_data/Patstat/CD2/tls202_part0'
for i in range(3):
    print 'file', i
    z = zipfile.ZipFile(path+str(i+1)+'.zip', 'r')
    tmp = csv.reader(z.open(z.infolist()[0]), delimiter=',')
    tmp.next()
    cnt = 0
    for j in tmp:
        if cnt % 1000000 == 0:
            print cnt
        if j[0] in appln_id:
            print j
            appln_title[j[0]] = j[1]
        cnt += 1

with open('tmp_title.dat', 'w') as f_out:
    for i in appln_title.keys():
        f_out.write('%s %s\n' % (i, appln_title[i]))
f_out.close()
