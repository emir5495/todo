import json
'''
data = {"ad":"emir", "yas": 18, "diller" : ["python","c"]}
json_string = json.dumps(data)
print(json_string)
'''
'''
json_str = '{"ad":"emir","yas":18}'
data = json.loads(json_str)
print(data["ad"])
'''
data = {"site": "OpenAI", "durum": True}
with open("veri.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)