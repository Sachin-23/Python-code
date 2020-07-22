### Assignment 3
#### Sum of n numbers
```python3
	sum = 0; n = 1
	while n != 0:
	    n = int(input("Enter the value of number you want to add (Enter '0' to stop) : "))
	    sum += n
	print("The total sum is", sum)
```
```bash
$ python sum.py
Enter the value of number you want to add (Enter '0' to stop) : 5
Enter the value of number you want to add (Enter '0' to stop) : 3
Enter the value of number you want to add (Enter '0' to stop) : 5
Enter the value of number you want to add (Enter '0' to stop) : 3
Enter the value of number you want to add (Enter '0' to stop) : 0
The total sum is 16
```

#### Find if whether the number is prime number or not
```python3
	n = int(input("Enter a number: "))
	r_n = int(n ** 0.5); i = 2;
	while i <= r_n :
	    if n % i == 0:
	        print("Number is a Prime number")
	        exit()
	    i += 1
	print("Number is not a prime number")
```
```bash
$ python prime.py
Enter a number: 43
Number is not a prime number
$ python prime.py
Enter a number: 7919
Number is not a prime number
$ python prime.py
Enter a number: 4
Number is a Prime number
$ python prime.py
Enter a number: 800
Number is a Prime number
