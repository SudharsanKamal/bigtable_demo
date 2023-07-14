from google.cloud import bigtable


project_name = 'prefab-botany-385705'
instance_name = 'demobt'
client = bigtable.Client(project=project_name, admin=True)
instance = client.instance(instance_name)
table = instance.table('student')

rows=[]
row_key = "102"
row = table.row(row_key)

row.set_cell('stu_info', 'name', "susan")
row.set_cell('stu_info', 'age', "23")
row.set_cell('stu_info', 'address', "123")
row.set_cell('stu_info', 'class', "12B")
row.set_cell('stu_info', 'gender', "Male")
row.set_cell('stu_marks', 'mark1', "98")
row.set_cell('stu_marks', 'mark2', "85")
row.set_cell('stu_marks', 'mark3', "83")
row.set_cell('stu_marks', 'total', "266")
row.set_cell('stu_marks', 'grade', "A")

rows.append(row)

table.mutate_rows(rows)
