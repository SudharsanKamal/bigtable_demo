import csv
from google.cloud import bigtable

project_name = 'prefab-botany-385705'
instance_name = 'demobt'
file = 'students.csv'

client = bigtable.Client(project=project_name, admin=True)
instance = client.instance(instance_name)
table = instance.table('student')
rows = []

with open(file) as fh:
    rd = csv.DictReader(fh, delimiter=',')
    for line in rd:
        line = dict(line)
        row_key = line['rollno']
        row = table.row(row_key)
        row.set_cell('stu_info', 'name', line['name'])
        row.set_cell('stu_info', 'age', line['age'])
        row.set_cell('stu_info', 'address', line['address'])
        row.set_cell('stu_info', 'class', line['class'])
        row.set_cell('stu_marks', 'mark1', line['mark1'])
        row.set_cell('stu_marks', 'mark2', line['mark2'])
        row.set_cell('stu_marks', 'mark3', line['mark3'])
        row.set_cell('stu_marks', 'total', line['total'])
        row.set_cell('stu_marks', 'grade', line['grade'])
        rows.append(row)

table.mutate_rows(rows)