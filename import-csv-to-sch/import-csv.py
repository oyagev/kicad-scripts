import csv

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

for row in reader:
    # Try to locate the header row
    if args.column_reference in row:
        header_ok = True
        ref_col = row.index(args.column_reference)

    print row

if not header_ok:
    sys.stderr.write('Cannot find a header with reference field: "%s"\n' % (args.column_reference))
    sys.exit()

