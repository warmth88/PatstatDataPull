__author__ = 'Alexander Sheredin'

import csv
import datetime

SOURCE_FILE = "lista_studenti.txt"
TARGET_FILE = "lista_inventori_1r.txt"
NEW_TARGET_FILE = "risultato_inventori_1r.txt"
COLUMN_DELIMITER = '\t'


def scan_target(filename):
    target_list = []
    target_dict = {}
    with open(filename, 'rb') as target_csv:
        target_csv.seek(0)
        target_reader = csv.reader(target_csv, delimiter=COLUMN_DELIMITER)
        target_heading = target_reader.next()
        offset = len(target_heading)
        for row in target_reader:
            while len(row) < offset:
                row.append("")
            target_dict[row[0]] = [0]
            target_list.append(row)

    return target_heading, target_list, target_dict


def process_src_row(target_dict, name, surname, ids):
    for key in target_dict:
        s1 = name + ' ' + surname
        s2 = surname + ' ' + name
        if s1 in key or s2 in key:
            if not target_dict[key][0]:
                target_dict[key][0] = 1
                target_dict[key] += [name, surname] + ids
            else:
                # no need to scan the rest in this case
                continue


def main():
    # First, scan target file
    print "Script started %s" % str(datetime.datetime.now())
    print "Scanning %s" % TARGET_FILE
    headers, target_list, target_dict = scan_target(TARGET_FILE)

    print "Processing %s" % SOURCE_FILE
    # Process source file
    with open(SOURCE_FILE, 'rb') as source_csv:
        source_csv.seek(0)
        source_reader = csv.reader(source_csv, delimiter=COLUMN_DELIMITER)
        src_headers = source_reader.next()
        n = 0
        for row in source_reader:
            name_source = row[0]
            surname_source = row[1]
            row_length = len(row)
            ids = [row[i] for i in range(2, row_length)] if row_length > 2 else []
            process_src_row(target_dict, name_source, surname_source, ids)
            if n % 500 == 0 and n:
                print "%d lines of %s processed" % (n, SOURCE_FILE)
            n += 1

    print "Writing %s" % NEW_TARGET_FILE
    # write target file
    with open(NEW_TARGET_FILE, 'wb') as target_csv:
        target_csv.seek(0)
        writer = csv.writer(target_csv, delimiter=COLUMN_DELIMITER)
        writer.writerow(headers + ["matched"] + src_headers)
        for row in target_list:
            writer.writerow(row + target_dict.get(row[0], []))


if __name__ == "__main__":
    main()
