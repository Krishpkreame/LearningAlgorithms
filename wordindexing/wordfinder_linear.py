import json

with open("randomlistofword.json", "r") as f:
    data = json.load(f)


x = "le"
# while True:
#     x = input("Enter the first few chars of the word to search")
#     if len(x) >= 2:
#         break
#     else:
#         print("Mf stop being dumb n read")

z = (ord(x[0])*1000)+ord(x[1])
print("Z value is ", z)
for i in range(len(data["indexkey"])):
    if(z == data["indexkey"][i]):
        print(data["data"][i], data["indexkey"][i])
