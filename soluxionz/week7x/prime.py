def is_prime(num: int) -> bool:
    if num < 2:                  
        return False
    i = 2

    while i * i <= num:          
        if num % i == 0:       
            return False
        i += 1
    return True


n = int(input("Enter N: "))

if is_prime(n):
    print(n, "is prime.")
else:
    print(n, "is not prime.")


primes = []
total = 0
number = 2
while number <= n:
    if is_prime(number):
        primes.append(number)
        total += number
    number += 1

print("Primes up to", str(n) + ":", primes)
print("Sum of primes:", total)
