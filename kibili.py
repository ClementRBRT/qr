#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import random
from PIL import Image

if len(sys.argv) != 2:
    print("usage: python kibili.py <code>")
    exit()
code = sys.argv[1]
random.seed(code)

img = Image.open("./kibili.png")
w, h = img.size
w -= 1
h -= 1
px = img.load()

swap = [(random.randint(0, w), random.randint(0, h), random.randint(0, w), random.randint(0, h)) for i in range(10**6)]
for i, s in enumerate(swap):
    if i%1000 == 0:
        print(f"{100*i/len(swap)}%")
    p = px[s[0], s[1]]
    px[s[0], s[1]] = px[s[2], s[3]]
    px[s[2], s[3]] = p
print("100%")
img.save("./res.png")
