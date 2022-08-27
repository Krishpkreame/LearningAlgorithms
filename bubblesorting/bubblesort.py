import json
f = open('data.json')
data = json.load(f)
f.close()
ary = data["data"]
for x in range(len(ary)):
    s = True
    for y in range(len(ary) - 1):
        if ary[y] > ary[y + 1]:
            temp = ary[y]
            ary[y] = ary[y + 1]
            ary[y + 1] = temp
            s = False
    if s:
        break
print(ary)
