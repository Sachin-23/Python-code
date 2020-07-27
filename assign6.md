# Assignment 5

```python3
list1 = [1, 2, 3, 4, 5, 7, 8]
list2 = ["a", "b", "c", "d", "e"]

print({list1[i]:list2[j] for i in range(len(list1)) for j in range(len(list2)) if i == j})
```
```bash
$ python create_dict.py
{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
```
