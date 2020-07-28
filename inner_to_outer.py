#!/usr/bin/env python

l = [(1, 2, 3), [1, 2], ["a", "hit", "less"]]
l2 = []
for i in l:
    for j in i:
        l2.append(j)
print(l2)
