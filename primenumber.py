## function to check if a number is prime or not.

import math as m

def isPrime(n):
    """This Functions checks if number is prime and return true if it is prime"""
    if n==1:     #since 1 is not a prime number
        return False
    
    for i in range(2, round(m.sqrt(n))): # if the number is not prime then it is divisible by a number less than it square root
        if n%i==0:
            return False
    else:
        return True


n = int(input('Enter a natural num to check if it is prime : '))

y = isPrime(n)  

if y == True:
    print("prime")
else:
    print("not prime")