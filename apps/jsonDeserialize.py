import json

json_string ='''{
    "name": "Eunice",
    "age": 30,
    "salary": 100000.0,
    "isMarried": true,
    "isHavingCar": null
}'''

emp_dict = json.loads(json_string)
print(type(emp_dict))

for k,v in emp_dict.items():
    print(k, ':', v)