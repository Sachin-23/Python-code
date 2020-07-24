#!/usr/bin/env python

# Attempt 1

l = [0, 1, 2, 10, 4, 1, 0, 56, 2, 0, 1, 3, 0, 56, 0, 4]
l.sort()
zero = l.count(0)
while zero:
    l.remove(0)
    l.append(0)
    zero -= 1
print(l)


# Attempt 2

def zero(n):
    if n != 0:
        return n
    else:
        return max_l + 1
        
l = [0, 1, 2, 10, 4, 1, 0, 56, 2, 0, 1, 3, 0, 56, 0, 4]
max_l = max(l)
l.sort(key=zero)
print(l)

# Attempt 3

l = [0, 1, 2, 10, 4, 1, 0, 56, 2, 0, 1, 3, 0, 56, 0, 4]
#print(sorted(l, key=[0, max(l)][n == 0]))
print(sorted(l, key=lambda x: return 0 if n == 0 else max(l)))