import csv
from google.cloud import bigtable

project_name = 'project-id'
instance_name = 'demobt'
file = 'emp.csv'

client = bigtable.Client(project=project_name, admin=True)
instance = client.instance(instance_name)
table = instance.table('employee')
rows = []

with open(file,'r', encoding='utf-8-sig') as fh:
    rd = csv.DictReader(fh, delimiter=',')
    for line in rd:
        line = dict(line)
        #print(line)
        row_key = line['emp_id']+"#"+line['department']
        #row_key is something that uniquely identifies the row. 
        #Here the row_key will be of the format "1#Marketing"

        row = table.row(row_key)

      # row.set_cell('column_family', 'column_qualifier', value)

        row.set_cell('pers_info', 'name', line['name'])
        row.set_cell('pers_info', 'age', line['age'])
        row.set_cell('pers_info', 'ph_no', line['ph_no'])
        row.set_cell('emp_info', 'designation', line['designation'])
        row.set_cell('emp_info', 'performance_rating', line['performance_rating'])
        row.set_cell('emp_info', 'salary', line['salary'])
       
        rows.append(row)

table.mutate_rows(rows)

print("Data Loaded Successfully")
