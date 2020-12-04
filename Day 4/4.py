import numpy as np

d = {}
with open("input.txt") as f:
    for line in f:
        # print(line, 'new line \n')
        items = line.split(' ')
        for i in items:
            print(i)
            (key, val) = i.split(':')
            d[key] = val