# Assignment 7

### Question 1

```python
port1 = {21: "FTP", 22: "SSH", 23: "telnet", 80: "http"}
print({port1[i]: i for i in port1})
```bash
$ python exchange_dict.py
{'FTP': 21, 'SSH': 22, 'telnet': 23, 'http': 80}
```

### Question 2

```python
tuple_in_list = [(1, 2), (3, 4), (4, 5)]
print([i[0] + i[1] for i in tuple_in_list])
```
```bash
$ python list_of_tuples.py
[3, 7, 9]
```

### Question 3

```python
l = [(1, 2, 3), [1, 2], ["a", "hit", "less"]]
l2 = []
for i in l:
    for j in i:
        l2.append(j)
print(l2)
```
```bash
$ python inner_to_outer.py
[1, 2, 3, 1, 2, 'a', 'hit', 'less']
```
