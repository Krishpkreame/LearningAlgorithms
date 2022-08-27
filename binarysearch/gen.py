import random
import json

num = 500000
x = 0
data = []

while True:
    if x > num:
        break
    temp = random.randint(0, num)
    if temp not in data:
        data.append(temp)
        x += 1

with open("data1.json", 'w') as f:
    json.dump(data, f)
