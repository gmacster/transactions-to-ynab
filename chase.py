import csv, sys

fieldnames = [
    'Date',
    'Payee',
    'Category',
    'Memo',
    'Outflow',
    'Inflow'
]

with open(sys.argv[1], newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames, lineterminator='\n')
    writer.writeheader()
    for row in reader:
        outflow = row['Amount'][0] == '-'
        writer.writerow({
            'Date': row['Post Date'],
            'Payee': row['Description'],
            'Category': row['Category'],
            'Memo': '',
            'Outflow' if outflow else 'Inflow': row['Amount'][1:] if outflow else row['Amount'],
        })
