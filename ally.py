import csv
import sys
from datetime import datetime

fieldnames = [
    'Date',
    'Payee',
    'Category',
    'Memo',
    'Outflow',
    'Inflow'
]

with open(sys.argv[1], newline='') as csv_file:
    reader = csv.DictReader(csv_file, skipinitialspace=True)
    writer = csv.DictWriter(
        sys.stdout, fieldnames=fieldnames, lineterminator='\n')
    writer.writeheader()
    for row in reader:
        outflow = row['Amount'][0] == '-'
        writer.writerow({
            'Date': datetime.strptime(row['Date'], '%Y-%m-%d').strftime('%m/%d/%Y'),
            'Payee': row['Description'],
            'Category': '',
            'Memo': row['Type'],
            'Outflow' if outflow else 'Inflow': row['Amount'][1:] if outflow else row['Amount'],
        })
