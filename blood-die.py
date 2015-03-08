#!/usr/bin/python

import json
from collections import namedtuple

json_data = open("blood-die.json")
list = json.load(json_data)

newlist = [elem for elem in list if elem[2].split()[0] == elem[3].split()[0]]
gelijkwoord = namedtuple("gelijkwoord", "language, word")

landlist = []
for i in newlist:
    languages = gelijkwoord(i[0], i[2])
    landlist.append(languages)
print(landlist)
