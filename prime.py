#!/usr/bin/env python

n = int(input("Enter a number: "))
r_n = int(n ** 0.5); i = 2;
while i <= r_n :
    if n % i == 0:
        print("Number is not a Prime number")
        exit()
    i += 1
print("Number is a prime number")
