import json

data = {"ad":"emir", "yas": 18, "diller" : ["python","c"]}
json_string = json.dumps(data)
print(json_string)