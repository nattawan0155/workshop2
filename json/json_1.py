import json

# some JSON:
json_string = '{ "name": "Yoshi & Asahi", "age":21.5,"city":"Japan"}'

# parse x:
python_dict = json.loads(json_string)

# the result is a Python dictionary:
print(python_ditc["name"])
print(python_ditc["age"])
print(python_ditc["city"])