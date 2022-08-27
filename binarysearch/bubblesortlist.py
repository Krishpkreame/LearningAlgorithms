import json

with open("data1.json", "r") as f:
    data = json.load(f)

for x in data["data"]:
    s = True
    for y in range(len(data["data"]) - 1):
        if data["data"][y] > data["data"][y+1]:
            temp = data["data"][y]
            data["data"][y] = data["data"][y+1]
            data["data"][y+1] = temp
            s = False
    if s:
        break

with open("data1.json", "w") as f:
    json.dump(data, f)
