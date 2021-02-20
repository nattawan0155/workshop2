import json

# a Python object (dict):
python_dict = {"name": "Yoshi & Asahi", "age": 21.5, "city": "Japan"}

# convert into JSON:
json_string = json.dump(python_dict)

# the result is a JSON string:
print(json_string)