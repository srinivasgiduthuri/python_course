# Create a function that takes a number and returns True if the number is prime
import random


def is_prime(number):
    if number == 1:
        return True
    else:
        for i in range(2, number // 2):
            if number % i == 0:
                return False
        else:
            return True


print(is_prime(29))
print(is_prime(7))
print(is_prime(30))
print(is_prime(1))
# Use that function with filter in order to select prime numbers from a list
# numbers = random.sample(range(1, 50), 10)
numbers = [44, 10, 39, 2, 7, 22, 15, 34, 14, 23]
print(numbers)
primes = filter(is_prime, numbers)
print(list(primes))
