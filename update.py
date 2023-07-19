from google.cloud import bigtable


project_name = 'project-id'
instance_name = 'demobt'
client = bigtable.Client(project=project_name, admin=True)
instance = client.instance(instance_name)
table = instance.table('employee')


row_key = '9#Marketing'
column_family_id = 'pers_info'


column_qualifier="name"
new_value="Susan"


row = table.row(row_key)


row.set_cell(column_family_id, column_qualifier, new_value)
table.mutate_rows([row])
