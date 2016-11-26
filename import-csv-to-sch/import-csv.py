import csv
import pprint

import sys
from sch.sch import Schematic
from sch.editor import ComponentEditor
import argparse


parser = argparse.ArgumentParser(description='')
parser.add_argument('--csv', dest='csv_file', required=True,
                    help='CSV file as input')
parser.add_argument('--col-ref', dest='column_reference', required=False, default="Reference",
                    help='Reference column name')
parser.add_argument('sch_filename', help='Schematic file as output', nargs='+')

args = parser.parse_args()

for fname in args.sch_filename:

    sch = Schematic(fname)
    sheets = sch.sheets

    sch_components = sch.components
    map_components = {}
    for c in sch_components:
        for f in c.fields:
            if int(f['id']) == 0:
                map_components[f['ref'].strip('"')] = c
                continue


    csvf = open(args.csv_file, 'r')
    reader = csv.reader(csvf)
    header_ok = False

    components = {}


    fields = reader.next()

    if args.column_reference in fields:
        refIndex = fields.index(args.column_reference)
        if refIndex != 0:
            sys.stderr.write('Reference field must be first column' )
            sys.exit()

    else:
        sys.stderr.write('Cannot find a title row with reference field: "%s"\n' % (args.column_reference))
        sys.exit()

    for row in reader:
        ref = row[0].strip()
        try:
            component = map_components[ref]
            ed = ComponentEditor(component)
            for i in range(len(row))[1:]:
                #if row[i] != '':
                ed.set_field_value(fields[i].strip(), row[i].strip())
            print 'Updated component %s from CSV in schematic file %s \n' % (ref, fname)
        except KeyError:
            pass

    sch.save()


