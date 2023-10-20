import json
import pprint

json_data = None
with open('file_name.txt', 'r') as f:
    data = f.read()
    json_data = json.loads(data)

print(json_data)
{"firstName": "John", "lastName": "Smith", "isAlive": "true", "age": 27, "address": {"streetAddress": "21 2nd Street", "city": "New York", "state": "NY", "postalCode": "10021-3100"}, 'children': []}

pprint.pprint(json_data)