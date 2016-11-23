import csv
import pprint

import sys
from sch.sch import Schematic
import argparse


parser = argparse.ArgumentParser(description='')
parser.add_argument('--csv', dest='csv_file', required=True,
                    help='CSV file as input')
parser.add_argument('--sch', dest='sch_file', required=True,
                    help='Schematic file as output')
parser.add_argument('--col-ref', dest='column_reference', required=False, default="Ref",
                    help='Reference column name')

args = parser.parse_args()

csvf = open(args.csv_file, 'r')
reader = csv.reader(csvf)
header_ok = False

components = {}


fields = reader.next()
#fields = map(str.strip, fields)


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
    if ref in components.keys():
        sys.stderr.write('Component with reference "%s" already exist on previous row\n' % (ref))
        sys.exit()

    components[ref] = {}

    for i in range(len(row))[1:]:
        if row[i] != '':
            components[ref][fields[i].strip()] = row[i].strip()

pprint.pprint(components)


