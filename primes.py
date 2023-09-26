"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def isPrime(number):
    if number == 1:
        return False
    else:
        for factor in range(2,number):
            if number % factor == 0:
                return False
    return True

def primes(number_of_primes):
    if(number_of_primes <= 0):
        raise ValueError("Only Positive Integer Worked")
    list = []
    currentNumber = 1
    for count in range(0,number_of_primes):
        while not isPrime(currentNumber):
            currentNumber += 1
        list.append(currentNumber)
        currentNumber += 1
    return list