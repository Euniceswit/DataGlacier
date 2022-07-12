import json

employee = {
    'name': 'John',
    'age': 55,
    'salary': 100000.0,
    'isMarried': True,
    'isHavingCar': None
}


json_string = json.dumps(employee, indent=4)  #returns a string
print(json_string)

with open('emp.json', 'w') as f:
    json.dump(employee,f,indent=4)