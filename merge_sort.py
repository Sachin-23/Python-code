def merge(l1, l2):
    i = 0; j = 0; k = 0; l3 = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i += 1
        else:
            l3.append(l2[j])
            j += 1
    if i == len(l1) - 1 and j != len(l2) - 1:
        l3.append(l2[j:])
    else :
        l3.append(l1[i:])
    return l3
l1 = [10, 20, 40, 60, 70, 80]
l2 = [5, 15, 25, 35, 45, 60]
print(merge(l1, l2))
