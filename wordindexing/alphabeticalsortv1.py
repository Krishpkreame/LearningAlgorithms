import json

with open("randomlistofword.json", "r") as f:
    data = json.load(f)

# alphabetically sorting the words
for i in data["data"]:
    s = True
    for y in range(len(data["data"]) - 1):
        v1 = (ord(data["data"][y].lower()[0])*1000) + \
            ord(data["data"][y].lower()[1])
        v2 = (ord(data["data"][y+1].lower()[0])*1000) + \
            ord(data["data"][y+1].lower()[1])
        if (v1 > v2):
            temp1 = data["data"][y]
            data["data"][y] = data["data"][y + 1]
            data["data"][y + 1] = temp1
            s = False
    if s:
        break

with open("randomlistofword.json", "w") as f:
    json.dump(data, f)
