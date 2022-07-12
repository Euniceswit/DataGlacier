from pyaml import yaml

emp_dict = {
    'name': 'EuniceSwit',
    'age': 30,
    'salary': 60000.0,
    'isMarried': True
}
#Serialization to yaml string
yaml_string = yaml.dump(emp_dict)
print(yaml_string)


#Serialization to yaml file
with open('emp.yaml', 'w') as f:
    yaml.dump(emp_dict, f)



#DeSerialization from yaml string
e_dict = yaml.safe_load(yaml_string)
print(e_dict)


#DeSerialization from yaml file
with open('emp.yaml', 'r') as f:
    e_dict_f = yaml.safe_load(f)

print(e_dict_f)