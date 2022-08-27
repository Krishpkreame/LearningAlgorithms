import json

with open("randomlistofword.json", "r") as f:
    data = json.load(f)

# INDEXING
tempkeydict = {"indexkey": []}
for i in data["data"]:
    tempx = (ord(i.lower()[0])*1000) + ord(i.lower()[1])
    tempkeydict["indexkey"].append(tempx)

# merge
data.update(tempkeydict)

with open("randomlistofword.json", "w") as f:
    json.dump(data, f)
