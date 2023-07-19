from google.cloud import bigtable

project_name = 'project-id'
instance_name = 'demobt'
client = bigtable.Client(project=project_name, admin=True)
instance = client.instance(instance_name)
table = instance.table('employee')

row_key = '3#HR'
row = table.row(row_key)
row.delete()
table.mutate_rows([row])
