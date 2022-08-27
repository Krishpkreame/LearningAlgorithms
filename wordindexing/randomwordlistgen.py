import json
from random_word import Wordnik
wordnik_service = Wordnik()

a = wordnik_service.get_random_words(limit=500)
s = wordnik_service.get_random_words(limit=500)
d = wordnik_service.get_random_words(limit=500)
f = wordnik_service.get_random_words(limit=500)
g = wordnik_service.get_random_words(limit=500)
h = wordnik_service.get_random_words(limit=500)
j = wordnik_service.get_random_words(limit=500)
k = wordnik_service.get_random_words(limit=500)
l = wordnik_service.get_random_words(limit=500)
m = wordnik_service.get_random_words(limit=500)

with open("randomlistofword.json", "w") as f:
    json.dump(a+s+d+f+g+h+j+k+l+m)
