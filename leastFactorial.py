#!/usr/bin/env python


def leastFactorial(n):
    ans = 1
    i = 2
    while ans <= n:
        ans *= i  
        i += 1 
    return ans

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(leastFactorial(n))

