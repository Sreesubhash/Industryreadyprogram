import json
d = {}
with open ("large-file.json", 'r', encoding= 'utf=8') as f:
    s = f.read()
    d = json.loads(s)

for keys in d:
    print(keys)
