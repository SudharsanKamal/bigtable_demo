import csv
from google.cloud import bigtable

project_name = 'project-id'
instance_name = 'demobt'


client = bigtable.Client(project=project_name, admin=True)
instance = client.instance(instance_name)
table = instance.table('employee')

column_family_id_1 = 'pers_info'
column_qualifier_1 = 'gender'

column_family_id_2 = 'emp_info'
column_qualifier_2 = 'project'

rows=[]

with open('gender_and_project.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file,delimiter=',')
    
    for row in reader:
        line = dict(row)
        row_key = line['emp_id']+"#"+line['department']
        row = table.row(row_key)
        row.set_cell(column_family_id_1, column_qualifier_1, line['gender'])
        row.set_cell(column_family_id_2, column_qualifier_2, line['project_name'])
        rows.append(row)
        
table.mutate_rows(rows)

print('Columns added successfully.')
