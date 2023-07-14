from google.cloud import bigtable


project_name = 'prefab-botany-385705'
instance_name = 'demobt'
client = bigtable.Client(project=project_name, admin=True)
instance = client.instance(instance_name)
table = instance.table('employee')

rows=[]
row_key = "102#HR"
row = table.row(row_key)

row.set_cell('pers_info', 'name', 'Ravi')
row.set_cell('pers_info', 'age', '25')
row.set_cell('pers_info', 'ph_no', '1548165979')
row.set_cell('pers_info', 'gender', 'Male')
row.set_cell('emp_info', 'designation', 'Intern')
row.set_cell('emp_info', 'performance_rating', '4.5')
row.set_cell('emp_info', 'salary', '20000')


rows.append(row)

table.mutate_rows(rows)
