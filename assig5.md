### Assignment 5

**Question 1**
```python
l = [0, 1, 2, 10, 4, 1, 0, 56, 2, 0, 1, 3, 0, 56, 0, 4]
print(sorted(l, key=lambda x: x if x != 0 else max(l) + 1))
```
```bash
$ python sort0(2).py
[1, 1, 1, 2, 2, 3, 4, 4, 10, 56, 56, 0, 0, 0, 0, 0]
```

**Question 2**
```python
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
        l3 += l2[j:]
    else :
        l3 += l1[i:]
    return l3
l1 = [10, 20, 40, 60, 70, 80]
l2 = [5, 15, 25, 35, 45, 60]
print(merge(l1, l2))
```
```bash
$ python merge_sort.py
[5, 10, 15, 20, 25, 35, 40, 45, 60, 60, 70, 80]
```
