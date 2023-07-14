import csv
from google.cloud import bigtable

project_name = 'prefab-botany-385705'
instance_name = 'demobt'
file = 'emp.csv'

client = bigtable.Client(project=project_name, admin=True)
instance = client.instance(instance_name)
table = instance.table('employee')

column_family_id = 'pers_info'
column_qualifier = 'gender'
rows=[]

with open('gender.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file,delimiter=',')
    
    for row in reader:
        line = dict(row)
        row_key = line['emp_id']+"#"+line['department']
        row = table.row(row_key)
        row.set_cell(column_family_id, column_qualifier, line['gender'])
        rows.append(row)
        
table.mutate_rows(rows)

print('Columns added successfully.')
