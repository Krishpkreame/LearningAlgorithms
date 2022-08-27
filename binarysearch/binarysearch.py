import json
import random
with open("data1.json", "r") as f:
    data = json.load(f)

number = random.randint(10, len(data["data"]) - 10)

lower = 0
upper = len(data["data"]) - 1

while upper >= lower:
    mid = lower + (upper - lower)//2

    if data["data"][mid] == number:
        print("FOUND: ", data["data"][mid])
        break
    elif data["data"][mid] < number:
        lower = mid + 1
    else:
        upper = mid - 1
