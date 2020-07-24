l = [0, 1, 2, 10, 4, 1, 0, 56, 2, 0, 1, 3, 0, 56, 0, 4]
#print(sorted(l, key=[0, max(l)][n == 0]))
print(sorted(l, key=lambda x: x if x != 0 else max(l) + 1))
