from google.cloud import bigtable

project_name = 'prefab-botany-385705'
instance_name = 'demobt'
client = bigtable.Client(project=project_name, admin=True)
instance = client.instance(instance_name)
table = instance.table('student')

row_key = '1'
column_family_id = 'stu_info'

row = table.row(row_key)
row.delete_cell(column_family_id,"address")

#To delete multiple cells/columns in a column family
#row.delete_cells(column_family_id,["age","class"])

table.mutate_rows([row]) 

# To delete columns in multiple rows

# for row_key in range(2,7):
#     row = table.row(str(row_key))
#     row.delete_cell(column_family_id,"address")
#     table.mutate_rows([row]) 


