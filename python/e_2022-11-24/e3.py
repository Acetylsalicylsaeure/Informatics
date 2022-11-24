# define the number to be counted from and an empty list
n = 2
primes = []


# define a function to check if there is a number in the range before n that
# divides it perfectly
def isprime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True


# check if n is prime, append to list and print
while n < 10000:
    if isprime(n) is True:
        primes.append(n)
        print(n)
    n += 1
print(primes)
