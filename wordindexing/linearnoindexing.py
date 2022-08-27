import json

with open("randomlistofword.json", "r") as f:
    data = json.load(f)

x = "po"
# while True:
#     x = input("Enter the first few chars of the word to search").lower()
#     if len(x) >= 2:
#         break
#     else:
#         print("Mf stop being dumb n read")

for i in data["data"]:
    if x == i[0:2].lower():
        print(i)
