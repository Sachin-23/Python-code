## Assignment 4

#### Question 1 

```python3
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
```
```bash
$ python find-method\(\).py
Enter a substring from 'what we think we become: we are Python programmer' : we
occurrence at 5
occurrence at 14
occurrence at 25
$ python find-method\(\).py
Enter a substring from 'what we think we become: we are Python programmer' : re
occurrence at 29
$ python find-method\(\).py
Enter a substring from 'what we think we become: we are Python programmer' : ew
substring not found in 'what we think we become: we are Python programmer'
```
#### Question 2

```python3
alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"	
spl = "~!@#$%^&*()"	
print(alpha.islower())
print(num.islower())
print(spl.islower())
print(alpha.isupper())
print(num.isupper())
print(spl.isupper())
```
```bash
$ python q2.py
True
False
False
False
False
False
```
+ `islower()` method - Return True if the string is a lowercase string, False otherwise.
+ `isupper()` method - Return True if the string is an uppercase string, False otherwise.
