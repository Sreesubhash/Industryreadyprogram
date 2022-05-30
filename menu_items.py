import json
with open("menu_items.json") as f:
    s = f.read()
    d = json.loads(s)

for cat in d:
    items = cat["menuItems"]
    if items:
        for item in items:
            print(cat["name"], item['name'])
    else: print(cat["name"], items)



import json
with open("menu_items.json") as f:
    s = f.read()
    d = json.loads(s)

for cat in d:
    print(cat["name"])



import json
with open("menu_items.json") as f:
    s = f.read()
    d = json.loads(s)

for cat in d:
    items = cat["menuItems"]
    if items:
        for subcat in items:
            print(subcat["name"])
