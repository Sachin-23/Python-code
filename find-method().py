#!/usr/bin/env python


i = 0;index = 0
s = "what we think we become: we are Python programmer"
s2 = input(f"Enter a substring from '{s}' : ", )
while i < len(s):
    index = s.find(s2, index, len(s)) 
    if index < 0: 
        if i <= 0:
            print("substring not found in '{0}'".format(s))
        break;
    print("occurrence at", index) 
    index += 1
    i = index
