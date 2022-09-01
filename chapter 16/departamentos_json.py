import json

# Load the data into a list
filename = 'departamentos.json'
with open (filename, encoding = 'utf8'):
	dep_data = json.load(f)


for dep_dict in dep_data:
	if dep_dict['provincia'] == 'Buenos Aires'