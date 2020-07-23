### Basic Syntax

```python
>>> print("Hello, World!")
Hello, World!
```

### Backslash

```python
>>> print("Hello, \
    world!")
```

### Formatted Output

```python
>>> name = "Camaro" 
>>> model = "zl1"
>>> year = 2020
>>> print("The name of car is %s, model is %s, Year is %d"%(name, model, year)) #old string formatting method.
The name of car is Camaro , model is zl1 , Year is 2020
```

```python
>>> print(f"The name of car is {name}, model is {model}, Year is {year}")
The name of car is Camaro, model is zl1, Year is 2020
```

```python
a = 20
_a = 23
print(a, _a)
20 23
```


## Operators

### Arithmetic 

```python
>>> a= 20
>>> b = 30
>>> add = a + b
>>> div = a / b
>>> sub = a - b
>>> mul = a * b
>>> floor = a // b
>>> print(f"Addition is {add}\nSubraction is {sub}\nDivision is {div}\nMultiplication is {mul}\nExponent is {expo}\nFloor Division is {floor}")
Addition is 50
Subtraction is -10
Division is 0.6666666666666666
Multiplication is 600
Exponent is 1073741824000000000000000000000000000000
Floor is 0
```

### Comparison

```python
>>> a = 20
>>> b = 50
>>> a == b
False
```

```python
>>> a != b
True
```

```python
>>> a > b
False
```

```python
>>> a < b
True
```

```python
>>> a>=b
False
>>> a<=b
True
```

### Assignment

```python
>>> a = 2
>>> b = 5
>>> a += b
>>> print(a)
7
```

```python3
>>> a -= b
>>> print(a)
```

```python3
>>> a **= b
>>> print(a)
32
```

```python3
>>> a *= b
print(a)
7
```

```python3
>>> a /= b
print(a)
32.0
```

### Bitwise


```python3
>>> a = 240
>>> b = 1
>>> a | b
241
```

```python3
a & b
0
```

### Logical 


```python3
>>> a = 50
>>> b = 40
>>> a > b and a == b
True
```

```python3
>>> a < b or a != b
```

```python3
>>> a > b a ==b
False
```

```python3
>>> a > b a != b
True
```

```python3
>>> not a > b and a != b
False
```

### Membership

```python3
>>> str="LetsUpgradePythonEssentials"
>>> "x" in str
False
>>> "l" in str
True
>>> "U" in st
True
>>> "z" in str
False
>>> ("z" in str) or ("x" in str)
False
```

### Identity

```python3
>>> a = 20
>>> b = 20
>>> a == b
True
>>> a is b 
True
>>> id(a) 
140275556023008
>>> a = 562
>>> b = 526
>>> a is b
False
>>> id(a)
140275556023104
>>> id(b)
```
