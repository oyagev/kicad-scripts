# kicad-scripts
A set of scripts to make kicad easier to work with.


## Import CSV (BOM) to Kicad .sch file
This script reads your BOM (CSV format) and update the schematic files:
* You can specify only one BOM file
* You can specify multiple sch files, in case your project use hierarchical sheets
* The script match each row to a single component by the "Reference" value. 
  The script is tested with the Reference column first on the BOM
* BOM file must have a first header row - each column is a component's field name
* The script will update each component it can match, updating all fields from BOM to SCH. 
  * Missing fields will be added to the comopnent.
  * Empty-value fields in the BOM will be updated on the SCH using the same logic, i.e. empty field on the BOM will result with an value-less field on the compnent.


```bash
usage: import-csv.py [-h] --csv CSV_FILE [--col-ref COLUMN_REFERENCE] sch_filename [sch_filename ...]

positional arguments:
  sch_filename          Schematic file as output

optional arguments:
  -h, --help            show this help message and exit
  --csv CSV_FILE        CSV file as input
  --col-ref COLUMN_REFERENCE
                        Reference column name
```

## Requirements and Installation
* Clone this repository
* Optional and recommended - use virtualenv
* pip install git+https://github.com/oyagev/kicad-library-utils
