#!/usr/bin/python

import sys
import xml.etree.ElementTree as ET
tree = ET.parse(sys.argv[1])
root = tree.getroot()

for i in root:
    start = float(i[13].text)
    if start < float(i[5].text) or start > float(i[7].text):
        root.remove(i)
for i in root:
    end = float(i[12].text)
    if end > float(i[7].text) or end < float(i[5].text):
        root.remove(i)

tree.write(sys.argv[2])