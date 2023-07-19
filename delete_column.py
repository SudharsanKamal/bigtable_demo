from google.cloud import bigtable

project_name = 'project-id'
instance_name = 'demobt'
client = bigtable.Client(project=project_name, admin=True)
instance = client.instance(instance_name)
table = instance.table('employee')

row_key = '7#HR'
column_family_id = 'pers_info'

row = table.row(row_key)
row.delete_cell(column_family_id,"age")

#To delete multiple cells/columns in a column family 

row_key = '11#HR'
row = table.row(row_key)
column_family_id = 'emp_info'
row.delete_cells(column_family_id,["project","salary"])
table.mutate_rows([row]) 

