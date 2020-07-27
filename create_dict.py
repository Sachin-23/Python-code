#!/usr/bin/env python

list1 = [1, 2, 3, 4, 5, 7, 8]
list2 = ["a", "b", "c", "d", "e"]

print({list1[i]:list2[j] for i in range(len(list1)) for j in range(len(list2)) if i == j})
