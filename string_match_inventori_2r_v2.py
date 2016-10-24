__author__ = 'Alexander Sheredin'

import csv
import datetime
from re import search

SOURCE_FILE = "lista_studenti.txt"
TARGET_FILE = "matched_inventori_1r.txt"
NEW_TARGET_FILE = "risultato_inventori_2r.txt"
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


"""
^name_source + " " + surname_source$
^surname_source + " " + name_source$

^name_source + " " + surname_source[\.,\(\); ] or other symbols
^surname_source + " " + name_source[\.,\(\); ] or other symbols

[\.,\(\); ]name_source + " " + surname_source$
[\.,\(\); ]surname_source + " " + name_source$

[\.,\(\); ]name_source + " " + surname_source[\.,\(\); ]
[\.,\(\); ]surname_source + " " + name_source[\.,\(\); ]
"""


def build_pattern(name, surname):
    p_dict = {"name": name, "surname": surname}
    pattern = r"(^|[^a-zA-Z])((%(name)s %(surname)s)|(%(surname)s %(name)s))($|[^a-zA-Z])" % p_dict
    return pattern


max_matches = 1
# Will init later, anyway. Number of columns in the source
src_headers_length = 10


def process_src_row(target_dict, name, surname, ids):
    global max_matches
    global src_headers_length
    for key in target_dict:
        pattern = build_pattern(name, surname)
        if search(pattern, key):
            if not target_dict[key][0]:
                target_dict[key][0] = 1
            else:
                # add empty idN entries
                while len(target_dict[key][1:]) % src_headers_length:
                    target_dict[key].append("")

                # update number of max_matches
                max_matches = max(max_matches, 1 + len(target_dict[key][1:]) /
                                  src_headers_length)

            target_dict[key] += [name, surname] + ids


def main():
    global src_headers_length
    global max_matches
    # First, scan target file
    start_time = datetime.datetime.now()
    print "Script started %s" % str(start_time)
    print "Scanning %s" % TARGET_FILE
    headers, target_list, target_dict = scan_target(TARGET_FILE)

    print "Processing %s" % SOURCE_FILE

    # Process source file
    with open(SOURCE_FILE, 'rb') as source_csv:
        source_csv.seek(0)
        source_reader = csv.reader(source_csv, delimiter=COLUMN_DELIMITER)
        src_headers = source_reader.next()
        src_headers_length = len(src_headers)
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

        additional_columns = []
        # additional columns added only if there are 2 or more matches
        # for some lines
        if max_matches >= 2:
            for i in xrange(1, max_matches):
                additional_columns += [("%d_" % (i + 1)) + h for h in src_headers]
        headers += ["matched"] + src_headers + additional_columns
        writer.writerow(headers)
        for row in target_list:
            writer.writerow(row + target_dict.get(row[0], []))

    end_time = datetime.datetime.now()
    print "Script ended %s" % str(end_time)


if __name__ == "__main__":
    main()
