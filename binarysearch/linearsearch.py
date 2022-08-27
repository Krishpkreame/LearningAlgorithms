import json
import random
with open("data1.json", "r") as f:
    data = json.load(f)

number = random.randint(10, len(data["data"]) - 10)

for i in data["data"]:
    if number == i:
        print("FOUND ", i)
        break
